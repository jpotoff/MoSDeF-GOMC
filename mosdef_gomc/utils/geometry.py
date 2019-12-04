import numpy as np

import mbuild as mb
from mbuild.coordinate_transform import angle


def calc_dihedral(point1, point2, point3, point4):
    """Calculates a dihedral angle

    Here, two planes are defined by (point1, point2, point3) and
    (point2, point3, point4). The angle between them is returned.

    Parameters
    ----------
    point1, point2, point3, point4 : array-like, shape=(3,), dtype=float
        Four points that define two planes

    Returns
    -------
    float
        The dihedral angle between the two planes defined by the four
        points.
    """
    points = np.array([point1, point2, point3, point4])
    x = np.cross(points[1] - points[0], points[2] - points[1])
    y = np.cross(points[2] - points[1], points[3] - points[2])
    return angle(x, y)


def coord_shift(xyz, box):
    """Ensures that coordinates are -L/2, L/2

    Checks if coordinates are -L/2, L/2 and then shifts coordinates
    if necessary. For example, if coordinates are 0, L, then a shift
    is applied to move coordinates to -L/2, L/2. If a shift is not
    necessary, the points are returned unmodified.

    Parameters
    ----------
    xyz : numpy.array of points with shape N x 3
    box : numpy.array specifing the size of box ie [Lx, Ly, Lz]

    Returns
    -------
    xyz : numpy.array of points with shape N x 3
    """
    box = np.asarray(box)
    assert box.shape == (3,)

    box_max = box/2.
    box_min = -box_max
    # Shift all atoms
    if np.greater(xyz, box_max).any():
        xyz -= box_max
    elif np.less(xyz, box_min).any():
        xyz += box_max

    return xyz

def wrap_coords(xyz, box):
    """ Wrap coordinates inside box

    Parameters
    ---------
    xyz : numpy.array of points with shape N x 3
    box : numpy.array specifing the size of box ie [Lx, Ly, Lz] or
        mb.Box

    Returns
    -------
    wrap_xyz : numpy.array of points with shape N x 3

    Notes
    -----
    Assumes we are wrapping inside the positive octant
    Currently only supports orthorhombic boxes
    """
    if not isinstance(box, mb.Box):
        box_arr = np.asarray(box)
        assert box_arr.shape == (3,)

        wrap_xyz = xyz - 1*np.floor_divide(xyz, box_arr) * box_arr
    else:
        xyz = xyz - box.mins  
        wrap_xyz = (xyz 
                - (1*np.floor_divide(xyz, box.lengths) * box.lengths)
                + box.mins)

    return wrap_xyz
