from PIL import Image

# Open the image
image = Image.open('output_zone.jpg')

# Define the desired width and height for the enhanced image
new_width = image.width * 4
new_height = image.height * 4

# Resize the image using bilinear interpolation
enhanced_image = image.resize((new_width, new_height), Image.BILINEAR)

# Save the enhanced image
enhanced_image.save('output_interpolation.jpg')
