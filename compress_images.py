import os
from pathlib import Path
from PIL import Image

RAW_DIR = "raw-img"
OUT_DIR = "images"
MAX_DIMENSION = 1920  # resize so longest edge doesn't exceed this
JPEG_QUALITY = 85     # 1-100, higher = better quality, larger file


def compress_images():
    raw_path = Path(RAW_DIR)
    out_path = Path(OUT_DIR)

    if not raw_path.exists():
        print(f"'{RAW_DIR}/' directory not found. Create it and drop images inside.")
        return

    out_path.mkdir(parents=True, exist_ok=True)

    extensions = {".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".webp"}
    files = [f for f in raw_path.iterdir() if f.suffix.lower() in extensions]

    if not files:
        print(f"No image files found in '{RAW_DIR}/'.")
        return

    print(f"Found {len(files)} image(s). Compressing...\n")

    for file in sorted(files):
        try:
            img = Image.open(file)

            # Convert to RGB for JPEG (drops alpha channel if present)
            if img.mode in ("RGBA", "P", "LA"):
                img = img.convert("RGB")
            elif img.mode != "RGB":
                img = img.convert("RGB")

            # Resize if larger than max dimension
            w, h = img.size
            if max(w, h) > MAX_DIMENSION:
                scale = MAX_DIMENSION / max(w, h)
                new_size = (int(w * scale), int(h * scale))
                img = img.resize(new_size, Image.LANCZOS)

            # Save as optimized JPEG
            out_name = file.stem + ".jpg"
            out_file = out_path / out_name
            img.save(out_file, "JPEG", quality=JPEG_QUALITY, optimize=True)

            orig_kb = file.stat().st_size / 1024
            new_kb = out_file.stat().st_size / 1024
            reduction = ((orig_kb - new_kb) / orig_kb * 100) if orig_kb else 0

            print(f"  {file.name:30s}  {orig_kb:>8.1f} KB  →  {out_name:30s}  {new_kb:>8.1f} KB  ({reduction:>5.1f}% smaller)")

        except Exception as e:
            print(f"  Skipped {file.name}: {e}")

    print(f"\nDone. Compressed images saved to '{OUT_DIR}/'.")


if __name__ == "__main__":
    compress_images()
