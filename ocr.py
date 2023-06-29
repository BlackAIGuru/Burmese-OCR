from PIL import Image
import pytesseract
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
img = cv2.imread('input.jpg', 0)

# Check if image is loaded correctly
if img is None:
    print('Image could not be opened.')
    exit()

# # Increase contrast
# img = cv2.equalizeHist(img)

# # Binarization
# _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# # Noise Reduction
# img = cv2.medianBlur(img, 3)

# # Convert to PIL Image
# img = Image.fromarray(img)

# Now use pytesseract on the numpy array directly
text = pytesseract.image_to_string(img, lang='mya')

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
    
print(text)
