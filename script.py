import cv2
import pytesseract

# Read the image file
image = cv2.imread('download.png')

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

# Draw bounding boxes around the contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Extract text from the contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    roi = image[y:y + h, x:x + w]

    # Use Tesseract to extract text from the ROI
    text = pytesseract.image_to_string(roi)
    print(text)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
