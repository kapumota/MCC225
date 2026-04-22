from __future__ import annotations
import argparse
from pathlib import Path
import json
import pandas as pd
from datasets import load_dataset

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=str, default="data/processed/flickr30k_hf")
    parser.add_argument("--train-limit", type=int, default=512)
    parser.add_argument("--val-limit", type=int, default=128)
    parser.add_argument("--test-limit", type=int, default=128)
    args = parser.parse_args()

    out_root = Path(args.output_root)
    images_dir = out_root / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    ds = load_dataset("nlphuji/flickr30k", split="test")
    counters = {"train": 0, "val": 0, "test": 0}
    limits = {"train": args.train_limit, "val": args.val_limit, "test": args.test_limit}
    rows = []

    for row in ds:
        split = row["split"]
        if split not in limits or counters[split] >= limits[split]:
            continue
        filename = row["filename"]
        image = row["image"]
        save_path = images_dir / filename
        if not save_path.exists():
            image.save(save_path)
        rows.append({
            "image_id": f"flickr30k_{row['img_id']}",
            "filename": filename,
            "filepath": str(save_path.resolve()),
            "split": split,
            "caption": row["caption"][0],
            "label": "",
            "all_captions_json": json.dumps(row["caption"], ensure_ascii=False),
        })
        counters[split] += 1
        if all(counters[k] >= limits[k] for k in limits):
            break

    df = pd.DataFrame(rows)
    df.to_csv(out_root / "all.csv", index=False)
    for split in ["train", "val", "test"]:
        df[df["split"] == split].to_csv(out_root / f"{split}.csv", index=False)
    print("Saved:", out_root)
    print(df["split"].value_counts())

if __name__ == "__main__":
    main()
