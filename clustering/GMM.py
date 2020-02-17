import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

wine = datasets.load_wine()
X = wine.data[:, [9, 12]]

sc = StandardScaler()
X_std = sc.fit_transform(X)

model = GaussianMixture(n_components=3, covariance_type="diag", random_state=1)
model.fit(X_std)
model2 = GaussianMixture(n_components=3, covariance_type="full", random_state=1)
model2.fit(X_std)

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)

x = np.linspace(X_std[:, 0].min(), X_std[:, 0].max(), 100)
y = np.linspace(X_std[:, 0].min(), X_std[:, 0].max(), 100)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -model.score_samples(XX)
Z = Z.reshape(X.shape)

plt.contour(X, Y, Z, levels=[0.5, 1, 2, 3, 4, 5])
plt.scatter(X_std[:, 0], X_std[:, 1], c=model.predict(X_std))
plt.scatter(model.means_[:, 0], model.means_[:, 1], s=250, marker="*", c="red")
plt.title("GMM(covariance_type=diag)")

plt.subplot(2, 1, 2)

x = np.linspace(X_std[:, 0].min(), X_std[:, 0].max(), 100)
y = np.linspace(X_std[:, 0].min(), X_std[:, 0].max(), 100)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -model2.score_samples(XX)
Z = Z.reshape(X.shape)

plt.contour(X, Y, Z, levels=[0.5, 1, 2, 3, 4, 5])
plt.scatter(X_std[:, 0], X_std[:, 1], c=model2.predict(X_std))
plt.scatter(model2.means_[:, 0], model2.means_[:, 1], s=250, marker="*", c="red")
plt.title("GMM(covariance_type=full)")

plt.show()