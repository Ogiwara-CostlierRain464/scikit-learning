import matplotlib.pyplot as plt
import numpy as np

from prml.clustering.k_means import KMeans
from prml.rv.multivariate_gaussian_mixture import MultivariateGaussianMixture

# training data
x1 = np.random.normal(size=(100, 2))
x1 += np.array([-5, -5])
x2 = np.random.normal(size=(100, 2))
x2 += np.array([5, -5])
x3 = np.random.normal(size=(100, 2))
x3 += np.array([0, 5])
x_train = np.vstack((x1, x2, x3))

x0, x1 = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
x = np.array([x0, x1]).reshape(2, -1).T# training data

k_means = KMeans(n_clusters=3)
k_means.fit(x_train)
cluster = k_means.predict(x_train)

plt.scatter(x_train[:, 0], x_train[:, 1], c=cluster)
plt.scatter(k_means.centers[:, 0], k_means.centers[:, 1], s=200, marker="X", lw=2, c=["purple", "cyan", "yellow"], edgecolors="white")
plt.contourf(x0, x1, k_means.predict(x).reshape(100, 100), alpha=0.1)
plt.show()

gmm = MultivariateGaussianMixture(n_components=3)
gmm.fit(x_train)
p = gmm.classify_probability(x_train)

plt.scatter(x_train[:, 0], x_train[:, 1], c=p)
plt.scatter(gmm.mu[:, 0], gmm.mu[:, 1], s=200, marker="X", lw=2, c=["red", "green", "blue"], edgecolor="white")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect("equal")
plt.show()