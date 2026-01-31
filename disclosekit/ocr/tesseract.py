# disclosekit/ocr/tesseract.py

import pytesseract
from disclosekit.ocr.engine import OCREngine


class TesseractEngine(OCREngine):
    def __init__(self, dpi: int = 300):
        self.dpi = dpi

    def ocr_page(self, page):
        """
        Run Tesseract OCR on a single pdfplumber page.
        """

        # Render the page to a PIL image (pdfplumber-native)
        pil_image = page.to_image(resolution=self.dpi).original

        # Run OCR
        data = pytesseract.image_to_data(
            pil_image,
            output_type=pytesseract.Output.DICT
        )

        words = data.get("text", [])
        confs = data.get("conf", [])

        text = " ".join(w for w in words if isinstance(w, str) and w.strip())

        # Robust confidence aggregation
        valid_confs = []
        for c in confs:
            try:
                ci = int(c)
                if ci >= 0:
                    valid_confs.append(ci)
            except (ValueError, TypeError):
                pass

        confidence = (
            sum(valid_confs) / len(valid_confs) / 100
            if valid_confs else 0.0
        )

        return {
            "engine": "tesseract",
            "engine_version": str(pytesseract.get_tesseract_version()),
            "confidence": confidence,
            "text": text,
        }
