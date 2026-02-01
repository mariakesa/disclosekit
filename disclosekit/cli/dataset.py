import argparse
from pathlib import Path

from disclosekit.ingest.scan import scan_dataset
from disclosekit.build.dataset import build_dataset_json
from disclosekit.ocr.tesseract import TesseractEngine


def main():
    parser = argparse.ArgumentParser(
        description="Process one Epstein dataset folder into JSON"
    )
    parser.add_argument("dataset", type=Path, help="Dataset folder (e.g. DataSet6)")
    parser.add_argument("--out", type=Path, required=True)

    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    docs = scan_dataset(args.dataset)
    ocr = TesseractEngine()

    out_path = args.out / f"{args.dataset.name}.json"

    build_dataset_json(
        dataset_id=args.dataset.name,
        docs_meta=docs,
        dataset_root=args.dataset.parent,
        ocr_engine=ocr,
        out_path=out_path,
    )

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
