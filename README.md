# Image Processing Automation Script

## Project Overview

This project automates the conversion and processing of icon images provided in TIFF format. The goal is to prepare these images for product launch by:

- Converting TIFF (and TIFF-like) images to JPEG format
- Rotating images to fix incorrect orientation (rotated 90° anti-clockwise)
- Resizing images from 192x192 pixels to 128x128 pixels
- Ensuring images are in RGB color mode for compatibility

## Why This Project?

The design contractor provided icon images in the wrong format and orientation. Due to deadline constraints and lack of communication with the contractor, an automated Python script was needed to process all images quickly and reliably.

## How It Works

The script scans the input folder for images (even those without file extensions), opens them using Pillow (PIL), and performs the following steps:

1. Image Mode Conversion
   - Some TIFF images use color modes such as "1", "L", "P", or "CMYK". These modes can cause issues during processing or saving. The script converts all images to "RGB" mode before further processing.

2. Rotation
   - Since the images were rotated 90° anti-clockwise by mistake, the script rotates them 90° clockwise (using `rotate(-90, expand=True)`).

3. Resizing
   - All images are resized to 128x128 pixels as per the project requirement.

4. Saving
   - Images are saved in the output folder in JPEG format with the `.jpeg` extension.

## Common Issue: Black Images After Processing

### What Happened?

Some input images were almost entirely black with some white/gray areas. After processing, these images turned fully black.

### Why?

This was due to the way Pillow handled image modes and transparency in certain TIFF images. When images in palette mode ("P") or grayscale ("L") were processed without proper conversion, the alpha channels or palette mappings got lost. This caused the pixel data to be interpreted incorrectly, resulting in all-black output images.

### How It Was Fixed?

- The script now converts all images to "RGB" mode before rotation and resizing.
- This conversion ensures that the color information and transparency are properly handled.
- The fix prevents loss of image details during processing.


