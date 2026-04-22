from __future__ import annotations
from typing import Dict, List
import numpy as np

def compute_similarity_matrix(image_features: np.ndarray, text_features: np.ndarray) -> np.ndarray:
    return image_features @ text_features.T

def ranks_from_similarity(sim: np.ndarray) -> np.ndarray:
    ranks = []
    for i in range(sim.shape[0]):
        order = np.argsort(-sim[i])
        rank = int(np.where(order == i)[0][0]) + 1
        ranks.append(rank)
    return np.array(ranks)

def summarize_ranking(sim: np.ndarray) -> Dict[str, float | List[int]]:
    ranks = ranks_from_similarity(sim)
    return {
        "R@1": float(np.mean(ranks <= 1)),
        "R@5": float(np.mean(ranks <= min(5, len(ranks)))),
        "R@10": float(np.mean(ranks <= min(10, len(ranks)))),
        "MRR": float(np.mean(1.0 / ranks)),
        "MeanRank": float(np.mean(ranks)),
        "MedianRank": float(np.median(ranks)),
        "Ranks": ranks.tolist(),
    }
