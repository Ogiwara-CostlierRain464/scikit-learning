from prml.rv.rv import RandomVariable


class MultivariateGaussianMixture(RandomVariable):
    def __init__(self,
                 n_components: int,
                 mu=None,
                 cov=None,
                 coef=None):
        super().__init__()
        self.n_components = n_components
        self.mu = mu
        self.cov = cov
        self.coef = coef


