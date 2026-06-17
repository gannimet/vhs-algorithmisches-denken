from PIL import Image

square_width = 200
destination_image = Image.new("RGB", (8 * square_width, 8 * square_width))

for y in range(8):
    for x in range(8):
        if x % 2 == y % 2:
            top = y * square_width
            left = x * square_width
            
            destination_image.paste(
                (255, 255, 255),
                (left, top, left + square_width, top + square_width),
            )
        
destination_image.show()