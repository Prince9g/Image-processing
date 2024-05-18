import cv2
import pytesseract
import openpyxl
from openpyxl.utils.exceptions import IllegalCharacterError

# Read the image file
image = cv2.imread('nowyouknow.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract to extract text from the entire image
text = pytesseract.image_to_string(gray_image)

# Define a function to clean the text and remove illegal characters
def clean_text(text):
    # Replace illegal characters with a space
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in illegal_chars:
        text = text.replace(char, ' ')
    return text

# Clean the text
cleaned_text = clean_text(text)

# Split the cleaned text into individual lines
lines = cleaned_text.split('\n')

# Create a new Excel workbook and select the active worksheet
workbook = openpyxl.Workbook()

# Select the active sheet
sheet = workbook.active

# Write each line of text to a separate row in the Excel sheet
for i, line in enumerate(lines, start=1):
    try:
        sheet.cell(row=i, column=1).value = line
    except IllegalCharacterError:
        print(f"Illegal characters found in line {i}. Skipping.")
    except Exception as e:
        print(f"An error occurred while writing to the Excel sheet: {e}")

# Save the workbook
try:
    workbook.save('output.xlsx')
    print("Data has been successfully written to output.xlsx.")
except Exception as e:
    print(f"An error occurred while saving the workbook: {e}")
