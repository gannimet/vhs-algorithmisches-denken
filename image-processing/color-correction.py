from PIL import Image

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("RGB", source_image.size)
(image_width, image_height) = source_image.size

R_DELTA = 100
G_DELTA = 0
B_DELTA = 0

for y in range(image_height):
    for x in range(image_width):
        (r, g, b) = source_image.getpixel((x, y))
        
        new_r = min(255, r + R_DELTA)
        new_g = min(255, g + G_DELTA)
        new_b = min(255, b + B_DELTA)
        
        destination_image.putpixel(
            (x, y),
            (new_r, new_g, new_b)
        )
        
destination_image.show()