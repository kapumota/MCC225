from __future__ import annotations
import argparse, json
from pathlib import Path
import pandas as pd
from datasets import load_dataset, DownloadConfig
from PIL import Image

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output-root', required=True)
    p.add_argument('--split', default='test')
    p.add_argument('--limit', type=int, default=128)
    args = p.parse_args()

    out = Path(args.output_root)
    img_dir = out / 'images'
    img_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        ds = load_dataset(
            'nlphuji/flickr30k',
            split=args.split,
            download_config=DownloadConfig(resume_download=True),
        )
    except UnicodeDecodeError as exc:
        raise RuntimeError(
            "No se pudo leer la caché local de Hugging Face para Flickr30k. "
            "Limpia la caché y vuelve a ejecutar:\n"
            "  rm -rf ~/.cache/huggingface/datasets/nlphuji___flickr30k\n"
            "  rm -rf ~/.cache/huggingface/modules/datasets_modules/datasets/nlphuji*"
        ) from exc
    rows = []
    for idx, item in enumerate(ds.select(range(min(args.limit, len(ds))))):
        image = item['image']
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)
        fname = f'{args.split}_{idx:05d}.jpg'
        image.save(img_dir / fname)
        captions = item['caption'] if isinstance(item['caption'], list) else [item['caption']]
        rows.append({
            'image_id': f'{args.split}_{idx:05d}',
            'filename': fname,
            'filepath': str(Path('images') / fname),
            'split': args.split,
            'caption': captions[0],
            'label': '',
            'all_captions_json': json.dumps(captions, ensure_ascii=False),
        })
    pd.DataFrame(rows).to_csv(out / f'{args.split}.csv', index=False)
    print('Saved', out / f'{args.split}.csv')

if __name__ == '__main__':
    main()
