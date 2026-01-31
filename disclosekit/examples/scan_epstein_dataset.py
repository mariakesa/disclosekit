from pathlib import Path
from disclosekit.ingest.scan import scan_dataset
from disclosekit.pdf.validate import validate_document
from disclosekit.pdf.open import open_pdf
from disclosekit.pdf.text_native import native_text_length
from disclosekit.pdf.images import page_has_images
from disclosekit.pdf.classify import classify_page
from disclosekit.ocr.policy import should_ocr
from disclosekit.ocr.tesseract import TesseractEngine

DATASET_ROOT = Path("/home/maria/disclosekit/data/epstein/DataSet 6")

docs = scan_dataset(DATASET_ROOT)

print(f"Found {len(docs)} documents")

for doc in docs[:5]:
    pdf_path = DATASET_ROOT / doc["relative_path"]
    result = validate_document(pdf_path)

    print(
        doc["document_id"],
        "valid=",
        result["valid"],
        "pages=",
        result["page_count"],
    )


for doc in docs[:2]:  # inspect first 2 docs only
    pdf_path = DATASET_ROOT / doc["relative_path"]
    reader = open_pdf(pdf_path)

    print(f"\nDocument: {doc['document_id']}")

    for i, page in enumerate(reader.pages[:5], start=1):
        length = native_text_length(page)
        print(f"  Page {i}: native_text_length={length}")



for doc in docs[:2]:
    pdf_path = DATASET_ROOT / doc["relative_path"]
    reader = open_pdf(pdf_path)

    print(f"\nDocument: {doc['document_id']}")

    for i, page in enumerate(reader.pages[:5], start=1):
        text_len = native_text_length(page)
        has_img = page_has_images(page)

        print(
            f"  Page {i}: native_text_length={text_len}, has_images={has_img}"
        )


for doc in docs[:2]:
    pdf_path = DATASET_ROOT / doc["relative_path"]
    reader = open_pdf(pdf_path)

    print(f"\nDocument: {doc['document_id']}")

    for i, page in enumerate(reader.pages[:5], start=1):
        text_len = native_text_length(page)
        has_img = page_has_images(page)

        page_type = classify_page(text_len, has_img)
        ocr_flag = should_ocr(page_type)

        print(
            f"  Page {i}: type={page_type}, OCR={ocr_flag}"
        )

import pdfplumber
from disclosekit.pdf.classify import classify_page
from disclosekit.ocr.policy import should_ocr
from disclosekit.ocr.tesseract import TesseractEngine

ocr_engine = TesseractEngine()

pdf_path = DATASET_ROOT / docs[0]["relative_path"]

with pdfplumber.open(pdf_path) as pdf:
    print(f"\nDocument: {docs[0]['document_id']}")

    for i, page in enumerate(pdf.pages[:2], start=1):
        native_text = page.extract_text() or ""
        native_len = len(native_text)

        has_images = bool(page.images)

        page_type = classify_page(native_len, has_images)

        print(
            f"  Page {i}: type={page_type}, "
            f"native_text_length={native_len}, "
            f"has_images={has_images}"
        )

        if should_ocr(page_type):
            ocr = ocr_engine.ocr_page(page)
            print(
                f"    OCR confidence={ocr['confidence']:.2f}, "
                f"OCR text sample={ocr['text'][:80]!r}"
            )

