from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List

import pandas as pd

def load_metadata(csv_path: str | Path, root: str | Path | None = None) -> pd.DataFrame:
    csv_path = Path(csv_path)
    if root is None:
        root = csv_path.parent.parent if csv_path.parent.name != "" else Path(".")
    root = Path(root)
    df = pd.read_csv(csv_path)
    if "filepath" not in df.columns:
        raise ValueError("metadata CSV debe incluir una columna 'filepath'")
    df["filepath"] = df["filepath"].astype(str).apply(lambda p: str((root / p).resolve()) if not Path(p).is_absolute() else p)
    if "caption" not in df.columns:
        raise ValueError("metadata CSV debe incluir una columna 'caption'")
    if "all_captions_json" in df.columns:
        df["all_captions"] = df["all_captions_json"].apply(lambda x: json.loads(x) if isinstance(x, str) else [])
    else:
        df["all_captions"] = df["caption"].apply(lambda x: [x])
    return df

def explode_all_captions(df: pd.DataFrame) -> pd.DataFrame:
    rows: List[Dict[str, str]] = []
    for _, row in df.iterrows():
        captions = row.get("all_captions", None) or [row["caption"]]
        for idx, cap in enumerate(captions):
            rows.append({
                "image_id": row.get("image_id", ""),
                "filepath": row["filepath"],
                "caption_id": f'{row.get("image_id","img")}_{idx}',
                "caption": cap,
                "label": row.get("label", None),
            })
    return pd.DataFrame(rows)
