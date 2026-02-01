# disclosekit/cli/utils.py
from pathlib import Path

def ensure_out_dir(out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    return out
