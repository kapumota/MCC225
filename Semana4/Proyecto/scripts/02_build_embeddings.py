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
import pandas as pd

from src.dataset_utils import load_metadata
from src.openclip_utils import create_model, encode_image_paths, encode_texts
from src.io_utils import ensure_dir

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata-csv", required=True)
    parser.add_argument("--model-name", default="ViT-B-32")
    parser.add_argument("--pretrained", default="laion2b_s34b_b79k")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--output", default="outputs/embeddings/bootstrap_embeddings.npz")
    args = parser.parse_args()

    df = load_metadata(args.metadata_csv, root=Path("."))
    model, preprocess, tokenizer, device = create_model(args.model_name, args.pretrained)

    image_features = encode_image_paths(model, preprocess, df["filepath"].tolist(), device, batch_size=args.batch_size)
    text_features = encode_texts(model, tokenizer, df["caption"].tolist(), device, batch_size=max(args.batch_size, 32))

    out_path = Path(args.output)
    ensure_dir(out_path.parent)
    np.savez_compressed(
        out_path,
        image_features=image_features,
        text_features=text_features,
        metadata_csv_path=str(Path(args.metadata_csv).resolve()),
        model_name=args.model_name,
        pretrained=args.pretrained,
    )
    print("Embeddings guardados en ", out_path)

if __name__ == "__main__":
    main()
