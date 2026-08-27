from PIL import Image

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("RGB", source_image.size)
(image_width, image_height) = source_image.size
STEP_SIZE = 50

for y in range(image_height):
    for x in range(image_width):
        color = source_image.getpixel((x, y))
        destination_image.putpixel(
            (x, image_height - y - 1),
            color
        )
        
destination_image.show()