import argparse
from pathlib import Path

from disclosekit.ingest.scan import scan_dataset
from disclosekit.ingest.utils import resolve_dataset_content_root
from disclosekit.build.dataset import build_dataset_json


def main():
    parser = argparse.ArgumentParser(
        description="Process all Epstein datasets into JSON"
    )
    parser.add_argument("root", type=Path, help="Folder containing DataSet1..12")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help="Number of parallel worker processes (default: CPU count - 1)",
    )

    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

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
            dataset_root=content_root,
            out_path=out_path,
            workers=args.workers,
        )

        print(f"  → {out_path}")


if __name__ == "__main__":
    main()
