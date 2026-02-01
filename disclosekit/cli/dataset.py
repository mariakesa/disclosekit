import argparse
from pathlib import Path

from disclosekit.ingest.scan import scan_dataset
from disclosekit.ingest.utils import resolve_dataset_content_root
from disclosekit.build.dataset import build_dataset_json


def main():
    parser = argparse.ArgumentParser(
        description="Process one Epstein dataset folder into JSON"
    )
    parser.add_argument("dataset", type=Path, help="Dataset folder (e.g. DataSet 6)")
    parser.add_argument("--out", type=Path, required=True)

    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help="Number of parallel worker processes (default: CPU count - 1)",
    )

    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    dataset_dir = args.dataset.resolve()
    dataset_root = resolve_dataset_content_root(dataset_dir)

    docs = scan_dataset(dataset_dir)

    out_path = args.out / f"{dataset_dir.name}.json"

    build_dataset_json(
        dataset_id=dataset_dir.name,
        docs_meta=docs,
        dataset_root=dataset_root,
        out_path=out_path,
        workers=args.workers,
    )


    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
