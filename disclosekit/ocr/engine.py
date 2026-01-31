# disclosekit/ocr/engine.py

from abc import ABC, abstractmethod
from typing import Dict


class OCRResult(Dict):
    """
    Dict-like container for OCR results.
    Expected keys:
      - text
      - confidence
      - engine
      - engine_version
    """
    pass


class OCREngine(ABC):
    @abstractmethod
    def ocr_page(self, page) -> OCRResult:
        """
        Run OCR on a single PDF page.
        """
        raise NotImplementedError
