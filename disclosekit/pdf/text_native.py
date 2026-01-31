# disclosekit/pdf/text_native.py

from typing import Optional


def extract_native_text(page) -> Optional[str]:
    """
    Extract native (selectable) text from a PDF page.

    Returns:
        - string if text exists
        - None if no text layer is present or extraction fails
    """
    try:
        text = page.extract_text()
        if text is None:
            return None

        # Normalize whitespace
        text = text.strip()
        if not text:
            return None

        return text
    except Exception:
        # We do not propagate errors at this stage
        return None


def native_text_length(page) -> int:
    """
    Return length of native text on a page.
    Returns 0 if no native text exists.
    """
    text = extract_native_text(page)
    if text is None:
        return 0
    return len(text)
