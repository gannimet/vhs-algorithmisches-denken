from PIL import Image

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("RGB", source_image.size)
(image_width, image_height) = source_image.size

for y in range(image_height):
    for x in range(image_width):
        (r, g, b) = source_image.getpixel((x, y))
        brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
        #brightness = (r+g+b)//3
        destination_image.putpixel(
            (x, y),
            (brightness, brightness, brightness)
        )
        
destination_image.show()