import argparse
from pathlib import Path
import json

from disclosekit.build.document import build_document_json


def main():
    parser = argparse.ArgumentParser(
        description="Process a single PDF document into JSON"
    )
    parser.add_argument("pdf", type=Path, help="Path to PDF document")
    parser.add_argument("--out", type=Path, required=True, help="Output folder")

    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    pdf_path = args.pdf.resolve()
    dataset_root = pdf_path.parent

    doc_meta = {
        "document_id": pdf_path.name,
        "relative_path": pdf_path.name,  # relative to dataset_root
        "volume": None,
    }

    doc_json = build_document_json(
        dataset_root=dataset_root,
        doc_meta=doc_meta,
    )

    out_path = args.out / f"{pdf_path.stem}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(doc_json, f, indent=2)

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
