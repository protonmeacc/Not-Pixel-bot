from PIL import Image
import numpy as np


class ImageSimplifier:
    def __init__(self, hex_palette):
        # Storing the color palette
        self.palette = [self.hex_to_rgb(color) for color in hex_palette]

    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def find_closest_color(self, pixel):
        if len(pixel) == 4:  # If there is an alpha channel, ignore it
            pixel = pixel[:3]
        colors = np.array(self.palette)
        dist = np.sqrt(np.sum((colors - pixel) ** 2, axis=1))
        return tuple(colors[np.argmin(dist)])

    def simplify_image(self, input_image):
        # Ensure that we are working only with RGB
        if input_image.mode == 'RGBA':
            input_image = input_image.convert('RGB')

        # Iterate over each pixel in the image and replace it with the closest color
        new_image_data = [
            self.find_closest_color(pixel) for pixel in input_image.getdata()
        ]

        # Create a new image with reduced colors
        new_image = Image.new(input_image.mode, input_image.size)
        new_image.putdata(new_image_data)

        return new_image

