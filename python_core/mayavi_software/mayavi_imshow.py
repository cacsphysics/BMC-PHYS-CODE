import numpy as np
from mayavi.mlab import *


def test_imshow():
    """ Use imshow to visualize a 2D 10x10 random array.
    """
    s = np.random.random((10, 10))
    return imshow(s, colormap='gist_earth')


test_imshow()
