import cv2
import pytesseract
import numpy as np

# Read the image file
image = cv2.imread('my.img')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to remove noise
_, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Use Otsu's method to find the optimal threshold value
_, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Apply morphology to remove small objects
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find contours in the thresholded image
contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extract text from the contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    roi = image[y:y + h, x:x + w]

    # Use Tesseract to extract text from the ROI
    text = pytesseract.image_to_string(roi)
    print(text)

    # Draw bounding boxes around the text regions
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Detect objects in the image
img = cv2.imread("download.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with both text and object detection
cv2.imshow('Image', image)
cv2.imshow('detected.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()