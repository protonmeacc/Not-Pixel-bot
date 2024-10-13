class PixelMapper:
    def __init__(self, background_size):
        self.bg_width, self.bg_height = background_size

    @staticmethod
    def rgb_to_hex(rgb):
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2]).upper()

    def calculate_pixel_coordinates(self, input_image, start_x, start_y):
        img_width, img_height = input_image.size
        coordinates_with_colors = []

        # Iterate over each pixel in the small image
        for y in range(img_height):
            for x in range(img_width):
                # Calculate the coordinates on the background
                new_x = start_x + x
                new_y = start_y + y

                # Check if the coordinates are within the bounds of the background image
                if 0 <= new_x < self.bg_width and 0 <= new_y < self.bg_height:
                    # Insert the coordinates of the new pixel into the list
                    coordinates_with_colors.append((new_x, new_y, self.rgb_to_hex(input_image.getpixel((x, y)))))
        return coordinates_with_colors
