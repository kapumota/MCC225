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

import numpy as np
from src.dataset_utils import load_metadata
from src.retrieval import mine_hard_negatives

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--embeddings", required=True)
    parser.add_argument("--metadata-csv", required=True)
    parser.add_argument("--top-n", type=int, default=10)
    args = parser.parse_args()

    bundle = np.load(args.embeddings, allow_pickle=True)
    sim = bundle["image_features"] @ bundle["text_features"].T
    df = load_metadata(args.metadata_csv, root=Path("."))
    hard = mine_hard_negatives(sim, df, top_n=args.top_n)
    print(hard.to_string(index=False))

if __name__ == "__main__":
    main()
