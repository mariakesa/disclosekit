from pathlib import Path
from typing import List, Dict

from disclosekit.ingest.utils import resolve_dataset_content_root


def scan_dataset(dataset_root: Path) -> List[Dict]:
    """
    Recursively discover all PDF documents in a dataset directory.

    Handles DOJ-style nested dataset folders.
    """
    documents = []

    content_root = resolve_dataset_content_root(dataset_root)

    for pdf_path in content_root.rglob("*.pdf"):
        rel_path = pdf_path.relative_to(content_root)

        # Extract volume if present (VOLxxxx)
        volume = None
        for part in rel_path.parts:
            if part.upper().startswith("VOL"):
                volume = part
                break

        documents.append(
            {
                "document_id": pdf_path.name,
                "relative_path": str(rel_path),
                "volume": volume,
                "size_bytes": pdf_path.stat().st_size,
            }
        )

    return documents
