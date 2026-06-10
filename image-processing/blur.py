from PIL import Image

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("RGB", source_image.size)
(image_width, image_height) = source_image.size
BLUR_RADIUS = 10

for y in range(image_height):
    for x in range(image_width):
        (avg_r, avg_g, avg_b) = (0, 0, 0)
        block_count = 0
        
        for dx in range(-BLUR_RADIUS, BLUR_RADIUS + 1):
            for dy in range(-BLUR_RADIUS, BLUR_RADIUS + 1):
                if 0 <= x + dx < image_width and 0 <= y + dy < image_height:
                    block_count += 1
                    (source_r, source_g, source_b) = source_image.getpixel((x + dx, y + dy))
                    avg_r += source_r
                    avg_g += source_g
                    avg_b += source_b
                
        destination_image.putpixel(
            (x, y),
            (int(avg_r / block_count), int(avg_g / block_count), int(avg_b / block_count)),
        )
        
destination_image.show()