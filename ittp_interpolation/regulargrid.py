import itertools

import numpy


class RegularGrid(object):
    """
    Linear Multivariate Regular Grid interpolation in arbitrary dimensions.
    """

    def __init__(self, limits, breaks, values):
        # Ensure the number of break points matches the number of limits
        assert len(breaks) == len(limits), [len(breaks), len(limits)]

        # Initialize a list to hold all grid edges
        grid_edges = []
        for limit, break_points in zip(limits, breaks, strict=False):
            # Verify that break points are within the specified limits
            assert break_points == [] or numpy.all(numpy.asarray(break_points) > limit[0]), [break_points, limit[0]]
            assert break_points == [] or numpy.all(numpy.asarray(break_points) < limit[1]), [break_points, limit[1]]

            # Construct the grid edges by combining limits and break points
            grid = numpy.array([limit[0]] + list(break_points) + [limit[1]])
            grid_edges.append(grid)

            # Ensure break points are in ascending order
            assert numpy.all(grid[1:] > grid[:-1]), 'Breaks need to be ascending'

        self.grid = grid_edges  # Store the grid edges

        # Verify that the shape of values matches the expected dimensions
        assert values.shape == tuple([len(b) + 2 for b in breaks]), [values.shape, [len(b) + 2 for b in breaks]]

        self.values = values  # Store the interpolation values

    def __call__(self, *coords):
        """
        Perform interpolation at given coordinates.
        """
        # Initialize lists to store the indices and normalized distances to the lower edge
        indices = []
        norm_distances = []

        # Determine the relevant edges for each provided coordinate
        for coord, break_points in zip(coords, self.grid, strict=False):
            # Find the index of the lower edge using binary search
            index = numpy.searchsorted(break_points, coord) - 1
            index = numpy.where(index == -1, 0, index)  # Ensure the index is non-negative

            indices.append(index)  # Store the index of the lower edge
            # Normalize the distance to the lower edge
            norm_distance = (coord - break_points[index]) / (break_points[index + 1] - break_points[index])
            norm_distances.append(norm_distance)

        # Generate the Cartesian product of edge indices for interpolation
        edges = itertools.product(*[[index, index + 1] for index in indices])
        interpolated_value = 0.0  # Initialize the interpolated value

        for edge_indices in edges:
            weight = 1.0  # Initialize weight for the current edge
            # Calculate the weight based on normalized distances
            for edge_index, index, norm_distance in zip(edge_indices, indices, norm_distances, strict=False):
                weight *= numpy.where(edge_index == index, 1 - norm_distance, norm_distance)

            # Accumulate the weighted interpolated value
            interpolated_value += self.values[edge_indices] * weight

        return interpolated_value  # Return the final interpolated value


__doc__ = RegularGrid.__doc__
