from typing import Tuple

import numpy as np
from prml.linear.regression import Regression


class BayesianRegression(Regression):
    """
    Bayesian regression model

    w ~ N(w|0, alpha^(-1)I)
    y = X @ w
    t ~ N(t|X @ w, beta^(-1))
    """

    def __init__(self, alpha=1., beta=1.):
        self.alpha = alpha
        self.beta = beta
        self.w_mean = None
        self.w_precision = None
        self.w_cov = None

    def fit(self, X: np.ndarray, t: np.ndarray):
        """
        cf. (3.50)
        """
        mean_prev, precision_prev = self._get_prior(np.size(X, 1))
        w_precision = precision_prev + self.beta * X.T @ X

        # w_mean = np.linalg.inv(w_precision) @ (precision_prev @ mean_prev + self.beta * X.T @ t)
        w_mean = np.linalg.solve(
            w_precision,
            precision_prev @ mean_prev + self.beta * X.T @ t
        )

        self.w_mean = w_mean
        self.w_precision = w_precision
        # why not solve inv only at predict step?
        self.w_cov = np.linalg.inv(self.w_precision)

    def predict(self, X: np.ndarray):
        """
        cf. (3.58)
        """
        y = X @ self.w_mean
        y_var = 1 / self.beta + np.sum(X @ self.w_cov * X, axis=1)
        y_std = np.sqrt(y_var)
        return y, y_std

    def _is_prior_defined(self) -> bool:
        return (self.w_mean is not None) and (self.w_precision is not None)

    def _get_prior(self, n_dim: int) -> Tuple:
        if self._is_prior_defined():
            return self.w_mean, self.w_precision
        else:
            return np.zeros(n_dim), self.alpha * np.eye(n_dim)
