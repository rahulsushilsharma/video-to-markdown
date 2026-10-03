import cv2
import pytesseract


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
processed_img = preprocess_for_ocr("receipt.jpg")

# Pass the cleaned OpenCV matrix directly to PyTesseract
# Configuration uses Page Segmentation Mode 3 (Fully automatic page segmentation)
custom_config = r"--oem 3 --psm 3"
extracted_text = pytesseract.image_to_string(processed_img, config=custom_config)

print("--- Extracted Text ---")
print(extracted_text)
