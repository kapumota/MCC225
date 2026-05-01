from __future__ import annotations
import argparse
from pathlib import Path
import sys

PROJECT_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "src").is_dir()),
    Path(__file__).resolve().parent,
)
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import json
import numpy as np
import pandas as pd

from src.dataset_utils import load_metadata
from src.metrics import summarize_ranking
from src.retrieval import mine_hard_negatives
from src.io_utils import ensure_dir

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--embeddings", required=True)
    parser.add_argument("--metadata-csv", required=True)
    parser.add_argument("--output-json", default="outputs/metrics/retrieval_metrics.json")
    parser.add_argument("--hard-negatives-csv", default="outputs/metrics/hard_negatives.csv")
    parser.add_argument("--top-n-hard-negatives", type=int, default=10)
    args = parser.parse_args()

    bundle = np.load(args.embeddings, allow_pickle=True)
    image_features = bundle["image_features"]
    text_features = bundle["text_features"]
    sim = image_features @ text_features.T
    df = load_metadata(args.metadata_csv, root=Path("."))

    metrics = {
        "image_to_text": summarize_ranking(sim),
        "text_to_image": summarize_ranking(sim.T),
        "n_pairs": int(sim.shape[0]),
    }

    out_json = Path(args.output_json)
    ensure_dir(out_json.parent)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    hard_df = mine_hard_negatives(sim, df, top_n=args.top_n_hard_negatives)
    hard_path = Path(args.hard_negatives_csv)
    ensure_dir(hard_path.parent)
    hard_df.to_csv(hard_path, index=False)

    print(json.dumps(metrics, indent=2))
    print("Negativos duros guardados en", hard_path)

if __name__ == "__main__":
    main()
