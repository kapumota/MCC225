
from __future__ import annotations
import numpy as np
import pandas as pd

def topk_text_to_image(query_feature: np.ndarray, image_features: np.ndarray, metadata: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    scores = (query_feature @ image_features.T).squeeze()
    order = np.argsort(-scores)[:k]
    rows = []
    for rank, idx in enumerate(order, start=1):
        row = metadata.iloc[idx]
        rows.append({
            "rank": rank,
            "image_id": row.get("image_id", idx),
            "filepath": row["filepath"],
            "caption": row["caption"],
            "label": row.get("label", ""),
            "score": float(scores[idx]),
        })
    return pd.DataFrame(rows)

def topk_image_to_text(image_feature: np.ndarray, text_features: np.ndarray, metadata: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    scores = (image_feature @ text_features.T).squeeze()
    order = np.argsort(-scores)[:k]
    rows = []
    for rank, idx in enumerate(order, start=1):
        row = metadata.iloc[idx]
        rows.append({
            "rank": rank,
            "image_id": row.get("image_id", idx),
            "caption": row["caption"],
            "label": row.get("label", ""),
            "score": float(scores[idx]),
        })
    return pd.DataFrame(rows)

def mine_hard_negatives(sim: np.ndarray, metadata: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    candidates = []
    n = sim.shape[0]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            candidates.append({
                "image_index": i,
                "text_index": j,
                "score": float(sim[i, j]),
                "image_id": metadata.iloc[i].get("image_id", i),
                "text_image_id": metadata.iloc[j].get("image_id", j),
                "image_label": metadata.iloc[i].get("label", ""),
                "text_label": metadata.iloc[j].get("label", ""),
                "image_caption": metadata.iloc[i]["caption"],
                "negative_caption": metadata.iloc[j]["caption"],
                "image_filepath": metadata.iloc[i]["filepath"],
            })
    df = pd.DataFrame(candidates).sort_values("score", ascending=False).head(top_n)
    return df.reset_index(drop=True)
