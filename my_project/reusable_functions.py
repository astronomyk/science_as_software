import numpy as np


def make_dataset(n=100):
    """
    Returns n (x,y) coordinates according to a gaussian distribution

    Parameters
    ----------
    n : int

    Returns
    -------
    x, y : array

    """

    x = np.random.normal(size=n)
    y = np.random.normal(size=n)

    return x, y
