from abc import abstractmethod, ABCMeta

import numpy as np


class RandomVariable(object, metaclass=ABCMeta):
    """
    base class for random variables
    """

    def __init__(self):
        self.parameter = {}

    def __str__(self):
        tmp = f"{self.__class__.__name__}(\n"
        for key, value in self.parameter.items():
            tmp += (" " * 4)
            if isinstance(value, RandomVariable):
                tmp += f"{key}={value:8}"
            else:
                tmp += f"{key}={value}"
            tmp += "\n"
        tmp += ")"
        return tmp

    def __repr__(self):
        return self.__str__()

    def __format__(self, indent="4"):
        indent = int(indent)
        tmp = f"{self.__class__.__name__}(\n"
        for key, value in self.parameter.items():
            tmp += (" " * indent)
            if isinstance(value, RandomVariable):
                tmp += f"{key}=" + value.__format__(str(indent + 4))
            else:
                tmp += f"{key}={value}"
            tmp += "\n"
        tmp += (" " * (indent - 4)) + ")"
        return tmp

    @abstractmethod
    def fit(self, X: np.ndarray, **kwargs):
        """
        estimate parameter(s) of the distribution
        """
        pass

    @abstractmethod
    def pdf(self, X: np.ndarray):
        """
        compute probability density function
        p(X|parameter)
        """
        pass

    @abstractmethod
    def draw(self, sample_size: int = 1):
        """
        draw samples from the distribution
        """
        pass
