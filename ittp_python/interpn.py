from numpy import interp
from scipy.interpolate import interp1d


def interpn(*args, **kw):
    """Perform N-dimensional interpolation.

    Usage:
    ai = interpn(x, y, z, ..., a, xi, yi, zi, ...)

    Parameters:
    - x, y, z, ...: N-D grid coordinates defining the interpolation space.
    - a: Multi-dimensional array of values corresponding to the grid points.
    - xi, yi, zi, ...: Coordinates at which to interpolate the values.

    Returns:
    Interpolated values at the specified coordinates.
    """
    method = kw.pop('method', 'cubic')  # Set interpolation method, default is 'cubic'
    if kw:
        raise ValueError("Unknown arguments: %s" % kw.keys())

    nd = (len(args) - 1) // 2  # Calculate the number of dimensions
    if len(args) != 2 * nd + 1:
        raise ValueError("Wrong number of arguments")

    grid_coords = args[:nd]  # Extract the grid coordinates
    points_to_interpolate = args[nd + 1:]  # Extract interpolation points
    values = args[nd]  # Extract the values to interpolate

    for j in range(nd):
        # Interpolate the values along each dimension
        values = interp1d(grid_coords[j], values, axis=j, kind=method)(points_to_interpolate[j])

    return values


def npinterpn(*args, **kw):
    """Perform N-dimensional interpolation.

    Usage:
    ai = npinterpn(x, y, z, ..., a, xi, yi, zi, ...)

    Parameters:
    - x, y, z, ...: N-D grid coordinates defining the interpolation space.
    - a: Multi-dimensional array of values corresponding to the grid points.
    - xi, yi, zi, ...: Coordinates at which to interpolate the values.

    Returns:
    Interpolated values at the specified coordinates.
    """
    method = kw.pop('method', 'cubic')  # Set interpolation method, default is 'cubic'
    if kw:
        raise ValueError("Unknown arguments: %s" % kw.keys())

    nd = (len(args) - 1) // 2  # Determine the number of dimensions
    if len(args) != 2 * nd + 1:
        raise ValueError("Wrong number of arguments")

    grid_coords = args[:nd]  # Get grid coordinates for interpolation
    points_to_interpolate = args[nd + 1:]  # Get points where values will be interpolated
    values = args[nd]  # Get the array of values for interpolation

    for j in range(nd):
        # Perform interpolation along the specified dimension
        values = interp1d(grid_coords[j], values, axis=j, kind=method)(points_to_interpolate[j])

    return values


__doc__ = interpn.__doc__
