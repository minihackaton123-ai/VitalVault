"""VitalVault: prescription OCR proof of concept.

Reads text from a prescription photo. In the full app, this text would be
sent to an AI model to create a simple, multilingual summary.

Run:
    python prescription_ocr.py path/to/prescription.jpg

Needs the Tesseract program installed on your computer (see README).
"""
import os
import sys

import pytesseract
from PIL import Image

# Windows default install location (ignored if Tesseract is already on PATH)
WIN_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.name == "nt" and os.path.exists(WIN_PATH):
    pytesseract.pytesseract.tesseract_cmd = WIN_PATH


def read_prescription(path: str) -> str:
    img = Image.open(path).convert("L")  # grayscale helps OCR
    return pytesseract.image_to_string(img)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python prescription_ocr.py <image_path>")
        sys.exit(1)
    print(read_prescription(sys.argv[1]))
