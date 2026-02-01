import argparse
from pathlib import Path

from disclosekit.ingest.scan import scan_dataset
from disclosekit.build.dataset import build_dataset_json
from disclosekit.ocr.tesseract import TesseractEngine
from disclosekit.ingest.utils import resolve_dataset_content_root



def main():
    parser = argparse.ArgumentParser(
        description="Process all Epstein datasets into JSON"
    )
    parser.add_argument("root", type=Path, help="Folder containing DataSet1..12")
    parser.add_argument("--out", type=Path, required=True)

    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    ocr = TesseractEngine()

    for ds in sorted(args.root.iterdir()):
        if not ds.is_dir():
            continue
        if not ds.name.lower().startswith("dataset"):
            continue

        print(f"Processing {ds.name}…")

        out_path = args.out / f"{ds.name}.json"
        content_root = resolve_dataset_content_root(ds)

        docs = scan_dataset(ds)

        build_dataset_json(
            dataset_id=ds.name,
            docs_meta=docs,
            dataset_root=content_root,  # ✅ CORRECT
            ocr_engine=ocr,
            out_path=out_path,
        )

        print(f"  → {out_path}")


if __name__ == "__main__":
    main()
