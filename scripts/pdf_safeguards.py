#!/usr/bin/env python3
"""
PDF Safeguards for MomMom's Kitchen (Standalone Collection)

This module provides safeguards to prevent oversized PDFs from crashing
AI processing sessions. Large PDFs can overwhelm Claude's context or
cause API timeouts.

KNOWN LIMITS:
- Claude's Read tool can process PDFs but performance degrades with size
- Very large PDFs (>10MB or >100 pages) should be processed via text extraction
- Embedded images in PDFs may also hit dimension limits (>2000px)

Usage:
    python scripts/pdf_safeguards.py validate          # Validate all PDFs
    python scripts/pdf_safeguards.py status            # Show PDF status
    python scripts/pdf_safeguards.py info <file>       # Get detailed PDF info
    python scripts/pdf_safeguards.py extract <file>    # Extract text from PDF

The manifest file (pdf_manifest.json) helps AI assistants:
- Skip known problematic PDFs
- Use text-extracted versions instead
- Track which PDFs have been processed for recipes

Part of the Family Recipe Archive - Standalone Collection Repository
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Tuple

# Try to import PDF libraries
try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False

try:
    from pypdf import PdfReader
    PYPDF_AVAILABLE = True
except ImportError:
    try:
        from PyPDF2 import PdfReader
        PYPDF_AVAILABLE = True
    except ImportError:
        PYPDF_AVAILABLE = False


# Configuration - Size limits
MAX_FILE_SIZE_MB = 10           # Warn above this
MAX_FILE_SIZE_HARD_MB = 50      # Block above this
MAX_PAGES_SOFT = 100            # Warn above this
MAX_PAGES_HARD = 500            # Block above this
MAX_PAGE_DIMENSION = 2000       # Match image safeguards

MANIFEST_FILE = "pdf_manifest.json"

# PDF statuses
STATUS_UNVALIDATED = "unvalidated"
STATUS_VALID = "valid"              # Small enough to read directly
STATUS_LARGE = "large"              # Should use text extraction
STATUS_OVERSIZED = "oversized"      # Too large, must use text extraction
STATUS_BROKEN = "broken"            # Cannot be read
STATUS_EXTRACTED = "extracted"      # Text version available
STATUS_PROCESSED = "processed"      # Recipe extraction complete


def bytes_to_mb(size_bytes: int) -> float:
    """Convert bytes to megabytes."""
    return size_bytes / (1024 * 1024)


def format_size(size_bytes: int) -> str:
    """Format file size for display."""
    mb = bytes_to_mb(size_bytes)
    if mb >= 1:
        return f"{mb:.1f} MB"
    return f"{size_bytes / 1024:.1f} KB"


class PDFManifest:
    """Manages the PDF processing manifest for session resilience."""

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.manifest_path = data_dir / MANIFEST_FILE
        self.manifest = self._load_manifest()

    def _load_manifest(self) -> Dict:
        """Load existing manifest or create new one."""
        if self.manifest_path.exists():
            try:
                with open(self.manifest_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Corrupted manifest, creating backup and starting fresh")
                backup = self.manifest_path.with_suffix('.json.bak')
                self.manifest_path.rename(backup)

        return {
            "created": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "limits": {
                "max_file_size_mb": MAX_FILE_SIZE_MB,
                "max_file_size_hard_mb": MAX_FILE_SIZE_HARD_MB,
                "max_pages_soft": MAX_PAGES_SOFT,
                "max_pages_hard": MAX_PAGES_HARD,
                "max_page_dimension": MAX_PAGE_DIMENSION
            },
            "pdfs": {},
            "stats": {
                "total": 0,
                "valid": 0,
                "large": 0,
                "oversized": 0,
                "broken": 0,
                "extracted": 0,
                "processed": 0
            }
        }

    def save(self):
        """Save manifest to disk."""
        self.manifest["last_updated"] = datetime.now().isoformat()
        self._update_stats()

        with open(self.manifest_path, 'w') as f:
            json.dump(self.manifest, f, indent=2)

    def _update_stats(self):
        """Update summary statistics."""
        stats = {
            "total": 0,
            "valid": 0,
            "large": 0,
            "oversized": 0,
            "broken": 0,
            "extracted": 0,
            "processed": 0
        }

        for pdf_data in self.manifest["pdfs"].values():
            stats["total"] += 1
            status = pdf_data.get("status", STATUS_UNVALIDATED)

            if status == STATUS_VALID:
                stats["valid"] += 1
            elif status == STATUS_LARGE:
                stats["large"] += 1
            elif status == STATUS_OVERSIZED:
                stats["oversized"] += 1
            elif status == STATUS_BROKEN:
                stats["broken"] += 1
            elif status == STATUS_EXTRACTED:
                stats["extracted"] += 1
            elif status == STATUS_PROCESSED:
                stats["processed"] += 1

        self.manifest["stats"] = stats

    def scan_pdfs(self) -> List[Path]:
        """Find all PDF files in data directory."""
        pdfs = list(self.data_dir.glob("**/*.pdf"))
        pdfs += list(self.data_dir.glob("**/*.PDF"))
        return sorted(pdfs)

    def get_pdf_info(self, pdf_path: Path) -> Dict:
        """Get detailed information about a PDF file."""
        result = {
            "filename": pdf_path.name,
            "path": str(pdf_path.relative_to(self.data_dir)),
            "file_size": 0,
            "file_size_mb": 0.0,
            "page_count": None,
            "has_text": None,
            "max_page_width": None,
            "max_page_height": None,
            "status": STATUS_UNVALIDATED,
            "error": None,
            "validated_at": datetime.now().isoformat(),
            "recommendations": []
        }

        # Check file exists and get size
        try:
            result["file_size"] = pdf_path.stat().st_size
            result["file_size_mb"] = bytes_to_mb(result["file_size"])
        except OSError as e:
            result["status"] = STATUS_BROKEN
            result["error"] = f"Cannot access file: {e}"
            return result

        # Check file size limits
        if result["file_size_mb"] > MAX_FILE_SIZE_HARD_MB:
            result["status"] = STATUS_OVERSIZED
            result["recommendations"].append(
                f"File exceeds {MAX_FILE_SIZE_HARD_MB}MB hard limit. "
                "Text extraction required."
            )
        elif result["file_size_mb"] > MAX_FILE_SIZE_MB:
            result["status"] = STATUS_LARGE
            result["recommendations"].append(
                f"File exceeds {MAX_FILE_SIZE_MB}MB soft limit. "
                "Consider text extraction for better performance."
            )

        # Try to read PDF metadata
        page_count, dimensions, has_text, error = self._read_pdf_metadata(pdf_path)

        if error:
            if result["status"] == STATUS_UNVALIDATED:
                result["status"] = STATUS_BROKEN
            result["error"] = error
            return result

        result["page_count"] = page_count
        result["has_text"] = has_text
        if dimensions:
            result["max_page_width"] = dimensions[0]
            result["max_page_height"] = dimensions[1]

        # Check page count limits
        if page_count:
            if page_count > MAX_PAGES_HARD:
                result["status"] = STATUS_OVERSIZED
                result["recommendations"].append(
                    f"PDF has {page_count} pages (>{MAX_PAGES_HARD}). "
                    "Text extraction required."
                )
            elif page_count > MAX_PAGES_SOFT:
                if result["status"] == STATUS_UNVALIDATED:
                    result["status"] = STATUS_LARGE
                result["recommendations"].append(
                    f"PDF has {page_count} pages (>{MAX_PAGES_SOFT}). "
                    "Consider processing in page ranges."
                )

        # Check page dimensions
        if dimensions and (dimensions[0] > MAX_PAGE_DIMENSION or
                          dimensions[1] > MAX_PAGE_DIMENSION):
            result["recommendations"].append(
                f"Some pages exceed {MAX_PAGE_DIMENSION}px. "
                "Embedded images may not render correctly."
            )

        # Set final status if still unvalidated
        if result["status"] == STATUS_UNVALIDATED:
            result["status"] = STATUS_VALID

        # Check for existing text extraction
        text_path = pdf_path.with_suffix('.txt')
        html_path = pdf_path.with_suffix('.txt.html')
        if text_path.exists() or html_path.exists():
            if result["status"] in [STATUS_VALID, STATUS_LARGE]:
                result["status"] = STATUS_EXTRACTED
            result["text_file"] = str(
                (text_path if text_path.exists() else html_path)
                .relative_to(self.data_dir)
            )

        return result

    def _read_pdf_metadata(self, pdf_path: Path) -> Tuple[Optional[int],
                                                           Optional[Tuple[int, int]],
                                                           Optional[bool],
                                                           Optional[str]]:
        """
        Read PDF metadata using available libraries.
        Returns: (page_count, (max_width, max_height), has_text, error)
        """
        # Try PyMuPDF first (better metadata)
        if PYMUPDF_AVAILABLE:
            try:
                doc = fitz.open(str(pdf_path))
                page_count = len(doc)

                max_width = 0
                max_height = 0
                has_text = False

                # Sample first few pages for dimensions and text
                for i, page in enumerate(doc):
                    if i >= 5:  # Only check first 5 pages
                        break
                    rect = page.rect
                    max_width = max(max_width, int(rect.width))
                    max_height = max(max_height, int(rect.height))

                    text = page.get_text()
                    if text and text.strip():
                        has_text = True

                doc.close()
                return page_count, (max_width, max_height), has_text, None

            except Exception as e:
                return None, None, None, f"PyMuPDF error: {e}"

        # Fall back to pypdf/PyPDF2
        if PYPDF_AVAILABLE:
            try:
                reader = PdfReader(str(pdf_path))
                page_count = len(reader.pages)

                max_width = 0
                max_height = 0
                has_text = False

                # Sample first few pages
                for i, page in enumerate(reader.pages[:5]):
                    box = page.mediabox
                    max_width = max(max_width, int(float(box.width)))
                    max_height = max(max_height, int(float(box.height)))

                    text = page.extract_text()
                    if text and text.strip():
                        has_text = True

                return page_count, (max_width, max_height), has_text, None

            except Exception as e:
                return None, None, None, f"pypdf error: {e}"

        # No PDF library available
        return None, None, None, "No PDF library available (install pymupdf or pypdf)"

    def validate_all(self):
        """Validate all PDFs in the data directory."""
        pdfs = self.scan_pdfs()

        print(f"\nValidating {len(pdfs)} PDF file(s)...")
        print("=" * 60)

        for pdf_path in pdfs:
            print(f"\n{pdf_path.name}")
            print("-" * 40)

            info = self.get_pdf_info(pdf_path)
            key = info["path"]
            self.manifest["pdfs"][key] = info

            print(f"  Size: {format_size(info['file_size'])}")
            if info["page_count"]:
                print(f"  Pages: {info['page_count']}")
            if info["max_page_width"]:
                print(f"  Max dimensions: {info['max_page_width']}x{info['max_page_height']}px")
            if info["has_text"] is not None:
                print(f"  Has text layer: {'Yes' if info['has_text'] else 'No'}")
            print(f"  Status: {info['status'].upper()}")

            if info["error"]:
                print(f"  Error: {info['error']}")

            if info["recommendations"]:
                print("  Recommendations:")
                for rec in info["recommendations"]:
                    print(f"    - {rec}")

            if info.get("text_file"):
                print(f"  Text version: {info['text_file']}")

        self.save()
        print("\n" + "=" * 60)
        self.print_status()

    def print_status(self):
        """Print current manifest status."""
        stats = self.manifest.get("stats", {})

        print("\nPDF MANIFEST STATUS")
        print("=" * 40)
        print(f"Last updated: {self.manifest.get('last_updated', 'Never')}")
        print(f"\nPDF Files:")
        print(f"  Total:      {stats.get('total', 0)}")
        print(f"  Valid:      {stats.get('valid', 0)} (can read directly)")
        print(f"  Large:      {stats.get('large', 0)} (text extraction recommended)")
        print(f"  Oversized:  {stats.get('oversized', 0)} (text extraction required)")
        print(f"  Broken:     {stats.get('broken', 0)}")
        print(f"  Extracted:  {stats.get('extracted', 0)} (text version available)")
        print(f"  Processed:  {stats.get('processed', 0)} (recipes extracted)")

        # List problematic PDFs
        problem_pdfs = [
            (k, v) for k, v in self.manifest.get("pdfs", {}).items()
            if v.get("status") in [STATUS_LARGE, STATUS_OVERSIZED, STATUS_BROKEN]
        ]
        if problem_pdfs:
            print(f"\nPDFs Needing Attention:")
            for key, pdf in problem_pdfs:
                size = format_size(pdf.get("file_size", 0))
                pages = pdf.get("page_count", "?")
                print(f"  - {pdf['filename']}: [{pdf['status']}] {size}, {pages} pages")

    def extract_text(self, filename: str) -> bool:
        """Extract text from a PDF file."""
        # Find the PDF
        pdf_path = None
        for pdf in self.scan_pdfs():
            if pdf.name == filename or str(pdf).endswith(filename):
                pdf_path = pdf
                break

        if not pdf_path:
            print(f"PDF not found: {filename}")
            return False

        output_path = pdf_path.with_suffix('.txt')

        if PYMUPDF_AVAILABLE:
            try:
                doc = fitz.open(str(pdf_path))
                print(f"Extracting text from {pdf_path.name} ({len(doc)} pages)...")

                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(f"# Text extracted from: {pdf_path.name}\n")
                    f.write(f"# Extracted: {datetime.now().isoformat()}\n")
                    f.write(f"# Pages: {len(doc)}\n\n")

                    for i, page in enumerate(doc):
                        f.write(f"\n{'='*60}\n")
                        f.write(f"PAGE {i + 1}\n")
                        f.write(f"{'='*60}\n\n")
                        f.write(page.get_text())

                doc.close()
                print(f"Saved to: {output_path}")

                # Update manifest
                key = str(pdf_path.relative_to(self.data_dir))
                if key in self.manifest["pdfs"]:
                    self.manifest["pdfs"][key]["status"] = STATUS_EXTRACTED
                    self.manifest["pdfs"][key]["text_file"] = str(
                        output_path.relative_to(self.data_dir)
                    )
                    self.save()

                return True

            except Exception as e:
                print(f"Error extracting text: {e}")
                return False

        elif PYPDF_AVAILABLE:
            try:
                reader = PdfReader(str(pdf_path))
                print(f"Extracting text from {pdf_path.name} ({len(reader.pages)} pages)...")

                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(f"# Text extracted from: {pdf_path.name}\n")
                    f.write(f"# Extracted: {datetime.now().isoformat()}\n")
                    f.write(f"# Pages: {len(reader.pages)}\n\n")

                    for i, page in enumerate(reader.pages):
                        f.write(f"\n{'='*60}\n")
                        f.write(f"PAGE {i + 1}\n")
                        f.write(f"{'='*60}\n\n")
                        f.write(page.extract_text() or "[No text on this page]")

                print(f"Saved to: {output_path}")

                # Update manifest
                key = str(pdf_path.relative_to(self.data_dir))
                if key in self.manifest["pdfs"]:
                    self.manifest["pdfs"][key]["status"] = STATUS_EXTRACTED
                    self.manifest["pdfs"][key]["text_file"] = str(
                        output_path.relative_to(self.data_dir)
                    )
                    self.save()

                return True

            except Exception as e:
                print(f"Error extracting text: {e}")
                return False

        else:
            print("No PDF library available. Install pymupdf or pypdf:")
            print("  pip install pymupdf")
            print("  # or")
            print("  pip install pypdf")
            return False

    def mark_status(self, filename: str, status: str, notes: str = ""):
        """Mark a PDF with a specific status."""
        for key, data in self.manifest["pdfs"].items():
            if data.get("filename") == filename or key.endswith(filename):
                data["status"] = status
                data["status_updated"] = datetime.now().isoformat()
                if notes:
                    data["notes"] = notes
                self.save()
                print(f"Marked {filename} as {status}")
                return True

        print(f"PDF not found: {filename}")
        return False


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    # Find data directory
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / 'data'

    if not data_dir.exists():
        print(f"ERROR: Data directory not found: {data_dir}")
        sys.exit(1)

    manifest = PDFManifest(data_dir)

    if command == "validate":
        manifest.validate_all()

    elif command == "status":
        manifest.print_status()

    elif command == "info":
        if len(sys.argv) < 3:
            print("Usage: pdf_safeguards.py info <filename>")
            sys.exit(1)

        filename = sys.argv[2]
        for pdf in manifest.scan_pdfs():
            if pdf.name == filename or str(pdf).endswith(filename):
                info = manifest.get_pdf_info(pdf)
                print(f"\nPDF Information: {info['filename']}")
                print("=" * 50)
                print(f"Path: {info['path']}")
                print(f"Size: {format_size(info['file_size'])} ({info['file_size_mb']:.2f} MB)")
                if info['page_count']:
                    print(f"Pages: {info['page_count']}")
                if info['max_page_width']:
                    print(f"Max Page Size: {info['max_page_width']}x{info['max_page_height']}px")
                if info['has_text'] is not None:
                    print(f"Has Text Layer: {'Yes' if info['has_text'] else 'No (scanned images)'}")
                print(f"Status: {info['status'].upper()}")
                if info['error']:
                    print(f"Error: {info['error']}")
                if info['recommendations']:
                    print("\nRecommendations:")
                    for rec in info['recommendations']:
                        print(f"  - {rec}")
                if info.get('text_file'):
                    print(f"\nText Version: {info['text_file']}")
                return

        print(f"PDF not found: {filename}")

    elif command == "extract":
        if len(sys.argv) < 3:
            print("Usage: pdf_safeguards.py extract <filename>")
            sys.exit(1)
        manifest.extract_text(sys.argv[2])

    elif command == "mark":
        if len(sys.argv) < 4:
            print("Usage: pdf_safeguards.py mark <filename> <status> [notes]")
            print(f"Valid statuses: {STATUS_PROCESSED}, {STATUS_EXTRACTED}, {STATUS_BROKEN}")
            sys.exit(1)
        filename = sys.argv[2]
        status = sys.argv[3]
        notes = sys.argv[4] if len(sys.argv) > 4 else ""
        manifest.mark_status(filename, status, notes)

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == '__main__':
    main()
