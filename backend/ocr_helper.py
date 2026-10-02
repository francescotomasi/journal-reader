import os
import subprocess
from PIL import Image

def ocr_crop(img, box, psm=6):
    """
    box: (ymin, xmin, ymax, xmax) normalized 0-1000
    """
    w, h = img.size
    crop_box = (
        int(box[1] * w / 1000),
        int(box[0] * h / 1000),
        int(box[3] * w / 1000),
        int(box[2] * h / 1000),
    )
    cropped = img.crop(crop_box)
    cropped.save("/tmp/crop.png")
    cmd = [
        "/opt/homebrew/bin/tesseract",
        "/tmp/crop.png",
        "stdout",
        "--tessdata-dir", "/tmp",
        "-l", "ita",
        "--psm", str(psm)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout.strip()

print("Helper defined")
