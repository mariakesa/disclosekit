from pathlib import Path
from disclosekit.ingest.scan import scan_dataset
from disclosekit.ocr.tesseract import TesseractEngine
from disclosekit.build.dataset import build_dataset_json


DATASET_ROOT = Path("/home/maria/disclosekit/data/epstein/DataSet 6")
OUT = Path("outputs/epstein_dataset_6.json")

docs = scan_dataset(DATASET_ROOT)
ocr_engine = TesseractEngine()

build_dataset_json(
    dataset_id="epstein_dataset_6",
    docs_meta=docs,
    dataset_root=Path(DATASET_ROOT),
    ocr_engine=ocr_engine,
    out_path=OUT,
)
