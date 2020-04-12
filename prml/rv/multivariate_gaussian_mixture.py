from prml.rv.rv import RandomVariable
import numpy as np
from prml.clustering.k_means import KMeans


class MultivariateGaussianMixture:
    def __init__(self, n_components: int):
        self.n_components = n_components
        self.mu = None
        self.cov = None
        self.pi = None

    def fit(self, X: np.ndarray):
        cov = np.cov(X.T)
        # KMeansで大まかにμを決める
        kmeans = KMeans(self.n_components)
        kmeans.fit(X)
        self.mu = kmeans.centers
        self.cov = np.array([cov for _ in range(self.n_components)])
        self.pi = np.ones(self.n_components) / self.n_components
        for _ in range(3): # TODO 対数尤度の変化 or パラメーターの変化
            status = self.expectation(X)
            self.maximization(X, status)

    def expectation(self, X: np.ndarray):
        resps = self.pi * self._gauss(X, np.size(self.mu, 1))
        resps /= resps.sum(axis=-1, keepdims=True)
        return resps

    def maximization(self, X: np.ndarray, resps):
        Nk = np.sum(resps, axis=0)
        self.pi = Nk / len(X)
        self.mu = (X.T @ resps / Nk).T
        d = X[:, None, :] - self.mu
        self.cov = np.einsum(
            'nki,nkj->kij', d, d * resps[:, :, None]) / Nk[:, None, None]

    def _gauss(self, X: np.ndarray, n_dim):
        d = X[:, None, :] - self.mu
        D_sq = np.sum(np.einsum('nki,kij->nkj', d, self.cov) * d, -1)
        return (
            np.exp(-0.5 * D_sq) / np.sqrt(np.linalg.det(self.cov) * (2 * np.pi) ** n_dim)
        )

    def classify_probability(self, X: np.ndarray):
        return self.expectation(X)
