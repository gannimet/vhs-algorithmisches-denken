from PIL import Image

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("RGB", source_image.size)
(image_width, image_height) = source_image.size
STEP_SIZE = 50

for y in range(image_height):
    for x in range(image_width):
        (source_r, source_g, source_b) = source_image.getpixel((x, y))
        destination_image.putpixel(
            (image_width - x - 1, y),
            (source_r, source_g, source_b)
        )
        
destination_image.show()