# disclosekit/pdf/classify.py

from enum import Enum


class PageType(str, Enum):
    TEXT_ONLY = "text_only"
    IMAGE_ONLY = "image_only"
    MIXED = "mixed"
    EMPTY = "empty"


def classify_page(native_text_length: int, has_images: bool) -> PageType:
    """
    Classify a page based on native text and image presence.
    """
    if native_text_length > 0 and has_images:
        return PageType.MIXED
    if native_text_length > 0 and not has_images:
        return PageType.TEXT_ONLY
    if native_text_length == 0 and has_images:
        return PageType.IMAGE_ONLY
    return PageType.EMPTY
