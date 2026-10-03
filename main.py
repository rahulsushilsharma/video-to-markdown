import subprocess

import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

ffmpeg_path = "./ffmpeg/bin/ffmpeg.exe"
teseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
stage1_path = "stage1/1/"
image_file_name = "frame_"

command = ["./ffmpeg/bin/ffmpeg.exe -i ./source/1.mp4 -an output.mp4"]
# subprocess.run(command, shell=True, check=True)
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = teseract_path
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# print(pytesseract.image_to_string("test.jpg"))
count = 0000
print(str(count))


def preprocess_for_ocr(image_path):
    # 1. Load image
    img = cv2.imread(image_path)

    # 2. Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Apply median blur to reduce salt-and-pepper noise
    blur = cv2.medianBlur(gray, 3)

    # 4. Apply Otsu's thresholding (best for distinct foreground/background)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    return thresh


# Execute processing


# Pass the cleaned OpenCV matrix directly to PyTesseract
# Configuration uses Page Segmentation Mode 3 (Fully automatic page segmentation)
custom_config = r"--oem 3 --psm 6 -l eng"


def count_in_str(padding: int, cur: int) -> str:
    num = str(cur)
    final_padding = padding - len(num)

    for _ in range(final_padding):
        num = "0" + num
    return num


# for i in range(2, 19):
#     try:
#         image_path = stage1_path + image_file_name + count_in_str(4, i) + ".jpg"
#         print(image_path)
#         processed_img = preprocess_for_ocr(image_path)
#         extracted_text = pytesseract.image_to_string(
#             processed_img, config=custom_config
#         )

#         print(extracted_text)
#     except:
#         print("path not found")

from docling.document_converter import DocumentConverter

image_path = stage1_path + image_file_name + count_in_str(4, 2) + ".jpg"
converter = DocumentConverter()
result = converter.convert(image_path)
print(result.document.export_to_markdown())
