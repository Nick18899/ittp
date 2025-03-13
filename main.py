from ittp_python.cartesiangrid import CartesianGrid
from utils.image import show_image
from utils.parser import Parser


def module_cartesiangrid():
    """Run the Cartesian Grid interpolation module."""
    print("Cartesian module running...")

    # Parse the input data
    parser = Parser(description='Process images with CartesianGrid interpolation.', module_name='cartesiangrid')
    parser.make_parse()  # Execute the parsing process
    params = parser.get_params()  # Retrieve parameters from the parser

    image, limits, points = params['image'], params['limits'], params['points']  # Extract relevant parameters

    # Display the original image
    show_image(image)

    # Create a CartesianGrid instance with the specified limits and image data
    grid = CartesianGrid(limits, image)

    # Interpolate values at the given points using the Cartesian grid
    interpolated_value = grid(points[0], points[1], points[2])
    print(f'Interpolated value for given points: {interpolated_value}')


def module_interp():
    """Run the interpolation module."""
    print("Interpolation module running...")


def module_regulargrid():
    """Run the regular grid module."""
    print("Regular Grid module running...")
