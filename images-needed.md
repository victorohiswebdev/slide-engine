# Images Needed — FYP CODET Slide Deck (8 slides)

Place all images in `images/`. The deck renders cleanly with colored placeholders, but real photos elevate it significantly.

Use `compress_images.py` to convert and compress images from `raw-img/` → `images/`.

---

## Image List

| # | Filename | Slide | Description | Search Terms | Source |
|---|----------|-------|-------------|-------------|--------|
| 1 | `fyp-ai-farm.jpg` | Cover (00) | AI + agriculture concept — drone view of smart farm, tech-meets-field aesthetic, bright/natural lighting | `smart farming drone AI agriculture innovation` | unsplash.com |
| 2 | `fyp-soil.jpg` | Slide 01 | Dry, cracked soil close-up in sunlight | `dry cracked soil drought agriculture` | unsplash.com |
| 3 | `fyp-farmer.jpg` | Slide 01 | Farmer manually watering crops, traditional method | `farmer watering crops manual irrigation` | unsplash.com |
| 4 | `fyp-signal.jpg` | Slide 01 | Rural farmland with weak/no connectivity | `rural farmland no signal poor internet` | unsplash.com |
| 5 | `fyp-prototype.jpg` | Slide 03 | **Your own photo** — Raspberry Pi, sensors, wiring bench | N/A (use your hardware photo) | your camera |
| 6 | `fyp-farm-bg.jpg` | Slides 06, 07 | Wide aerial view of green farmland, calm composition | `smart farm aerial green field agriculture` | unsplash.com |
| 7 | `fyp-qr.png` | Slide 07 | QR code linking to your GitHub profile | Generate at qr-code-generator.com | N/A |

---

## Image Specifications

- **Aspect ratio**: Landscape (16:9 preferred)
- **Resolution**: At least 1200px wide (canvas is 1920×1080)
- **Format**: `.jpg` for photos, `.png` for QR code (keep crisp edges)
- **Tone**: Natural, warm, professional

---

## Notes

- `fyp-prototype.jpg` is the most impactful — this answers the unspoken judge question "is this real engineering?"
- `fyp-qr.png` should be a PNG, NOT compressed as JPEG (QR codes need sharp edges)
- Drop all source images into `raw-img/`, run `python compress_images.py`, and they land in `images/`
