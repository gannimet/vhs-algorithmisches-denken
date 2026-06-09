from PIL import Image

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("L", source_image.size)
(image_width, image_height) = source_image.size
THRESHOLD = 128

for y in range(image_height):
    for x in range(image_width):
        (r, g, b) = source_image.getpixel((x, y))
        brightness = 0.299 * r + 0.587 * g + 0.114 * b
        destination_image.putpixel(
            (x, y),
            255 if brightness > THRESHOLD else 0
        )
        
destination_image.show()