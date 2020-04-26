import numpy as np
import matplotlib.pyplot as plt

from prml.rv.variational_gaussian_mixture import VariationalGaussianMixture

x1 = np.random.normal(size=(100, 2))
x1 += np.array([-5, -5])
x2 = np.random.normal(size=(100, 2))
x2 += np.array([5, -5])
x3 = np.random.normal(size=(100, 2))
x3 += np.array([0, 5])
x_train = np.vstack((x1, x2, x3))

x0, x1 = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
x = np.array([x0, x1]).reshape(2, -1).T

vgmm = VariationalGaussianMixture(K=6)
vgmm.fit(x_train)

plt.scatter(x_train[:, 0], x_train[:, 1], c=vgmm.classify(x_train))
plt.xlim(-10, 10, 100)
plt.ylim(-10, 10, 100)
plt.show()
