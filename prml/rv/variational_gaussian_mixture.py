import numpy as np
from scipy.special import gamma, digamma, logsumexp


class VariationalGaussianMixture:
    def __init__(self, K=1):
        # Number of class
        self.K = K
        self.N = None
        # dimension of data
        self.D = None

        # ν
        self.nu = None
        self.nu0 = None
        self.W = None
        self.W0 = 1.
        self.alpha = None
        self.alpha0 = 1 / K
        self.beta = None
        self.beta0 = 1.
        self.m = None
        self.m0 = None

        # cf. P193
        self.alpha0 = 1 / self.K

    def fit(self, X: np.ndarray):
        self.init_params(X)
        for _ in range(1000):  # NOTE: 対数尤度の変化 or パラメーターの変化に応じて停止するようにすべき
            r = self.variational_expectation(X)
            self.variational_maximization(X, r)

    def init_params(self, X: np.ndarray):
        # sample_size = number of dataset(N)
        sample_size, self.D = X.shape
        self.alpha0 = np.ones(self.K) * self.alpha0
        self.m0 = np.mean(X, axis=0)
        self.W0 = np.eye(self.D) * self.W0
        self.nu0 = self.D

        self.N = sample_size / self.K + np.zeros(self.K)
        self.alpha = self.alpha0 + self.N  # (10.58)
        self.beta = self.beta0 + self.N   # (10.60)
        indices = np.random.choice(sample_size, size=self.K, replace=False)
        self.m = X[indices]
        self.W = np.tile(self.W0, (self.K, 1, 1))
        self.nu = self.nu0 + self.N  # (10.63)

    def variational_expectation(self, X: np.ndarray):
        # x_n - m_k
        d = X[:, np.newaxis] - self.m
        # (10.64)
        mahalanobis_exp = \
            self.D / self.beta \
            + self.nu * np.sum(np.einsum("kij,nkj->nki", self.W, d) * d, axis=-1)
        # (10.65)
        ln_lambda_exp = \
            digamma(0.5 * (self.nu - np.arange(self.D)[:, np.newaxis])).sum(axis=0) \
            + self.D * np.log(2) + np.linalg.slogdet(self.W)[1]
        # (10.66)
        ln_pi_exp = \
            digamma(self.alpha) - digamma(self.alpha.sum())

        # (10.46)
        ln_rho = ln_pi_exp + 0.5 * ln_lambda_exp - 0.5 * mahalanobis_exp
        # (10.49)
        ln_rho -= logsumexp(ln_rho, axis=-1)[:, np.newaxis]
        r = np.exp(ln_rho)
        return r

    def variational_maximization(self, X: np.ndarray, r: np.ndarray):
        # (10.51)
        self.N = r.sum(axis=0)
        # (10.52)
        x_m = (X.T.dot(r) / self.N).T
        # x_n - x_m
        d = X[:, np.newaxis] - x_m
        # (10.53)
        S = np.einsum("nki,nkj->kij", d, r[:, :, None] * d) / self.N[:, None, None]
        # (10.58)
        self.alpha = self.alpha0 + self.N
        # (10.60)
        self.beta = self.beta0 + self.N
        # (10.61)
        self.m = (self.beta0 * self.m0 + self.N[:, None] * x_m) / self.beta[:, None]
        # x_m - mo
        d = x_m - self.m0
        # (10.62)
        self.W = np.linalg.inv(
            np.linalg.inv(self.W0)
            + (self.N * S.T).T
            + (self.beta0 * self.N * np.einsum("ki,kj->kij", d, d).T / (self.beta0 + self.N)).T
        )
        # (10.63)
        self.nu = self.nu0 + self.N

    def classify(self, X: np.ndarray):
        return np.argmax(self.variational_expectation(X), 1)
