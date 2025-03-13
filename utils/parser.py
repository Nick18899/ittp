import argparse
from typing import Dict
import numpy as np
from .image import path_to_image
from .utils import parse_tuple

class Parser(argparse.ArgumentParser):
    """
    A parser class to handle command-line arguments for different modules.
    """

    def __init__(self, module_name: str = 'cartesiangrid', description: str = 'Argument parse process...'):
        super().__init__(description=description)  # Initialize the base class with a description
        self.module_name = module_name  # Store the name of the module for conditional parsing

    def make_parse(self):
        if self.module_name == 'cartesiangrid':
            # Add arguments specific to the cartesian grid module
            self.add_argument('--image_path', type=str, help='Path to the input image file', default=None)
            self.add_argument('--limits', type=list, help='Limits for the interpolation',
                              default=[(0, 1), (0, 1), (0, 1)])
            self.add_argument('--points', type=parse_tuple, help='Points for interpolation',
                              default=([0.1], [0.5], [0.3]))

        self.args = self.parse_args()

    def get_params(self) -> Dict:
        params = {}

        if self.module_name == 'cartesiangrid':
            # Load the image from the specified path or generate a random noise image if not provided
            if self.args.image_path:
                try:
                    image = path_to_image(self.args.image_path)  # Load the image
                except Exception as e:
                    print(f"Error loading image: {e}, using random noise image.")
                    image = np.random.rand(512, 512, 3)  # Create a random noise image if loading fails
            else:
                print("No image path provided. Using random noise image.")
                image = np.random.rand(512, 512, 3)  # Create a random noise image if no path is given

            # Retrieve limits and points from the parsed arguments
            limits = self.args.limits
            points = self.args.points

            params = {
                'image': image,
                'limits': limits,
                'points': points,
            }

        return params  # Return the collected parameters
