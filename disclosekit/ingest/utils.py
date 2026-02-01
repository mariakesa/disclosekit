from pathlib import Path

def resolve_dataset_content_root(dataset_root: Path) -> Path:
    """
    DOJ Epstein datasets are often nested as:
        DataSet X/
          └── DataSet X/
              └── VOL...

    This function returns the inner content root if present,
    otherwise returns dataset_root unchanged.
    """
    inner = dataset_root / dataset_root.name
    if inner.exists() and inner.is_dir():
        return inner
    return dataset_root
