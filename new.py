from PIL import Image

# Open the image file
img = Image.open(r"nowyouknow.jpg")

# Calculate the dimensions of the image
width, height = img.size

# Define the coordinates for cropping
left = width - 300  # 510 pixels from the right edge
top = height - 300  # 292 pixels from the bottom edge
right = width       # Right edge of the image
bottom = height -150    # Bottom edge of the image

# Crop the image
img_res = img.crop((left, top, right, bottom))

# Show the cropped image
img_res.show()