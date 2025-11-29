#!/usr/bin/env python3
import os
from PIL import Image, UnidentifiedImageError

old_path = r"/media/abdullah_khan/New Volume/Automation Projects/image-processing/images/"
new_path = r"/media/abdullah_khan/New Volume/Automation Projects/image-processing/processed/"

# Ensure processed directory exists
os.makedirs(new_path, exist_ok=True)

for filename in os.listdir(old_path):
    img_path = os.path.join(old_path, filename)

    # Skip folders
    if os.path.isdir(img_path):
        continue

    try:
        with Image.open(img_path) as img:
            print("Processing:", filename, "Mode:", img.mode)

            # Convert modes safely
            if img.mode in ["1", "L", "P", "CMYK"]:
                img = img.convert("RGB")
            elif img.mode != "RGB":
                img = img.convert("RGB")

            # Rotate and resize
            img = img.rotate(-90, expand=True).resize((128, 128))

            # Output name (add .jpeg)
            out_name = filename + ".jpeg"
            out_path = os.path.join(new_path, out_name)

            img.save(out_path, "JPEG")

    except UnidentifiedImageError:
        print("Skipping (not an image):", filename)

print("Done! All the images are processed.")




