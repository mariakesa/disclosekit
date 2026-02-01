import argparse
from pathlib import Path
import json

from disclosekit.build.document import build_document_json
from disclosekit.ocr.tesseract import TesseractEngine


def main():
    parser = argparse.ArgumentParser(
        description="Process a single PDF document into JSON"
    )
    parser.add_argument("pdf", type=Path, help="Path to PDF document")
    parser.add_argument("--out", type=Path, required=True, help="Output folder")

    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    doc_meta = {
        "document_id": args.pdf.name,
        "relative_path": str(args.pdf),
        "volume": None,
    }

    ocr = TesseractEngine()
    doc_json = build_document_json(
        doc_meta,
        dataset_root=Path("/"),
        ocr_engine=ocr,
    )

    out_path = args.out / f"{args.pdf.stem}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(doc_json, f, indent=2)

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
