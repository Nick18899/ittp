import numpy as np
import scipy.ndimage


class CartesianGrid(object):

    def __init__(self, bounds, data):
        self.data = data
        self.bounds = bounds

    def __call__(self, *positions):
        positions = np.asarray(positions)

        # Calculate pixel indices based on the positions and bounds
        pixel_indices = [
            (pos - lower) * (size - 1) / (upper - lower)
            for (lower, upper), pos, size in zip(self.bounds, positions, self.data.shape)
        ]

        return scipy.ndimage.map_coordinates(
            self.data,
            pixel_indices,
            cval=np.nan,
            order=1
        )


__doc__ = CartesianGrid.__doc__
