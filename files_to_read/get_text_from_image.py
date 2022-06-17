from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

import os

directory = r"."
with open("text.txt", "w") as w:
    print("Working on that...")
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            w.write(pytesseract.image_to_string(Image.open(filename)))
        else:
            continue

print("Done.")
