from PIL import Image
from math import sqrt

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("L", source_image.size)

G_x = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

G_y = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
]

(image_width, image_height) = source_image.size

for source_x in range(image_width):
    for source_y in range(image_height):
        x_edge = 0
        y_edge = 0
        
        for filter_x in [-1, 0, 1]:
            for filter_y in [-1, 0, 1]:
                mask_x = source_x + filter_x
                mask_y = source_y + filter_y
                
                if mask_x >= 0 and mask_x < image_width and mask_y >= 0 and mask_y < image_height:
                    # (r, g, b, a) = source_image.getpixel((mask_x, mask_y)) # mit Mode "RGBA"
                    (r, g, b) = source_image.getpixel((mask_x, mask_y))
                    source_brightness = 0.299 * r + 0.587 * g + 0.114 * b

                    x_edge += source_brightness * G_x[filter_y][filter_x]
                    y_edge += source_brightness * G_y[filter_y][filter_x]
                    
        destination_brightness = int(sqrt(x_edge ** 2 + y_edge ** 2))
        # destination_image.putpixel((source_x, source_y), (destination_brightness, destination_brightness, destination_brightness, a)) # mit Mode "RGBA"
        destination_image.putpixel((source_x, source_y), destination_brightness) # mit Mode "L"


destination_image.show()