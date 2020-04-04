import itertools
import functools
import numpy as np


class PolynomialFeature(object):
    """
    polynomial features

    Example
    =======
    x =
    [[a, b],
     [c, d]]

     y = PolynomialFeature(degree=2).transform(x)
     y =
     [[1, a, b, a^2, a*b, b^2],
      [1, c, d, c^2, c*d, d^2]]
    =======
    """

    def __init__(self, degree: int = 2):
        self.degree = degree

    def transform(self, x: np.ndarray):
        """
        :param x: (sample_size, n) ndarray
        :return: (sample_size, 1 + nC1 + … + nCd) ndarray
        """
        if x.ndim == 1:
            x = x[:, np.newaxis]
        x_t = x.T
        features = [np.ones(len(x))]
        for degree in range(1, self.degree + 1):
            for items in itertools.combinations_with_replacement(x_t, degree):
                features.append(functools.reduce(lambda x, y: x * y, items))
        return np.asarray(features).T
