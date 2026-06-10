from PIL import Image
from math import sqrt

filename = "mcdonald.jpeg"
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
                
                if 0 <= mask_x < image_width and 0 <= mask_y < image_height:
                    (r, g, b) = source_image.getpixel((mask_x, mask_y))
                    source_brightness = 0.299 * r + 0.587 * g + 0.114 * b

                    x_edge += source_brightness * G_x[filter_y + 1][filter_x + 1]
                    y_edge += source_brightness * G_y[filter_y + 1][filter_x + 1]
                    
        destination_brightness = min(255, int(sqrt(x_edge ** 2 + y_edge ** 2)))
        destination_image.putpixel((source_x, source_y), destination_brightness)


destination_image.show()