from PIL import Image

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("RGB", (source_image.size[1], source_image.size[0]))
(image_width, image_height) = source_image.size
STEP_SIZE = 50

for y in range(image_height):
    for x in range(image_width):
        (source_r, source_g, source_b) = source_image.getpixel((x, y))
        destination_image.putpixel(
            (y, x),
            (source_r, source_g, source_b)
        )
        
destination_image.show()