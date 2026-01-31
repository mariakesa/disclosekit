# disclosekit/ingest/scan.py

from pathlib import Path
from typing import List, Dict


def scan_dataset(dataset_root: Path) -> List[Dict]:
    """
    Recursively discover all PDF documents in a dataset directory.

    Returns a list of document descriptors with provenance.
    """
    documents = []

    for pdf_path in dataset_root.rglob("*.pdf"):
        rel_path = pdf_path.relative_to(dataset_root)

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
