# disclosekit/ocr/policy.py

from disclosekit.pdf.classify import PageType


def should_ocr(page_type: PageType) -> bool:
    """
    Decide whether OCR should be run on a page.
    """
    if page_type == PageType.IMAGE_ONLY:
        return True
    if page_type == PageType.MIXED:
        # OCR may capture annotations, stamps, handwriting
        return True
    return False
