from PIL import Image

image_width = 256 * 3
destination_image = Image.new("RGB", (image_width, image_width))

for y in range(image_width):
    for x in range(image_width):
        color = (x % 256, y % 256, 128)

        destination_image.putpixel((x, y), color)

destination_image.show()