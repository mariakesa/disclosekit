# disclosekit/pdf/validate.py

from pathlib import Path
from disclosekit.pdf.open import get_page_count, PDFOpenError


def validate_document(path: Path) -> dict:
    """
    Validate a PDF document and return basic facts.
    """
    try:
        page_count = get_page_count(path)
        return {
            "valid": True,
            "page_count": page_count,
            "error": None,
        }
    except PDFOpenError as e:
        return {
            "valid": False,
            "page_count": None,
            "error": str(e),
        }
