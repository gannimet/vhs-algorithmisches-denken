from PIL import Image

filename = "mountain-lake.jpeg"
source_image = Image.open(f"image-processing/img/{filename}")
destination_image = Image.new("RGB", source_image.size)
(image_width, image_height) = source_image.size
RASTER_SIZE = 15

for y in range(0, image_height, RASTER_SIZE):
    for x in range(0, image_width, RASTER_SIZE):
        (avg_r, avg_g, avg_b) = (0, 0, 0)
        block_count = 0
        
        for dx in range(RASTER_SIZE):
            for dy in range(RASTER_SIZE):
                if x + dx < image_width and y + dy < image_height:
                    block_count += 1
                    (source_r, source_g, source_b) = source_image.getpixel((x + dx, y + dy))
                    avg_r += source_r
                    avg_g += source_g
                    avg_b += source_b
                
        destination_image.paste(
            (int(avg_r / block_count), int(avg_g / block_count), int(avg_b / block_count)),
            (x, y, x + RASTER_SIZE, y + RASTER_SIZE),
        )
        
destination_image.show()