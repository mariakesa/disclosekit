# disclosekit/pdf/open.py

from pathlib import Path
from pypdf import PdfReader


class PDFOpenError(Exception):
    """Raised when a PDF cannot be opened or parsed."""
    pass


def open_pdf(path: Path) -> PdfReader:
    """
    Safely open a PDF file.

    Raises PDFOpenError if the file is not a valid PDF.
    """
    try:
        reader = PdfReader(path)
        # Force-load first page metadata to catch lazy errors
        _ = len(reader.pages)
        return reader
    except Exception as e:
        raise PDFOpenError(f"Failed to open PDF: {path}") from e


def get_page_count(path: Path) -> int:
    """
    Return the number of pages in a PDF.

    Raises PDFOpenError if invalid.
    """
    reader = open_pdf(path)
    return len(reader.pages)
