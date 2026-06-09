from PIL import Image

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("RGB", source_image.size)
(image_width, image_height) = source_image.size

for y in range(image_height):
    for x in range(image_width):
        (r, g, b) = source_image.getpixel((x, y))
        destination_image.putpixel(
            (x, y),
            (b, r, g)
        )
        
destination_image.show()