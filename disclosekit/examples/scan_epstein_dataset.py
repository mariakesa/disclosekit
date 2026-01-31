from pathlib import Path
from disclosekit.ingest.scan import scan_dataset
from disclosekit.pdf.validate import validate_document

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
