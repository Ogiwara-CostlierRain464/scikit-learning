import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR

np.random.seed(seed=0)
X = np.random.uniform(0, 4, 50)[:, None]
y = np.sin(1 / 4 * 2 * np.pi * X).ravel() + np.random.normal(0, 0.3, 50)

model = SVR(kernel="rbf", C=10000, gamma=0.1, epsilon=0.3)
model.fit(X, y)

plt.figure(figsize=(8, 4))

X_plt = np.arange(0, 4, 0.1)[:, None]
y_true = np.sin(1 / 4 * 2 * np.pi * X_plt).ravel()
y_pred = model.predict(X_plt)

plt.scatter(X, y, color="blue", label="data")
plt.plot(X_plt, y_true, color="lime", linestyle="-", label="True sin(x)")
plt.plot(X_plt, y_pred, color="red", linestyle="-", label="gamma=0.1")
plt.plot(X_plt, y_pred + model.epsilon, color="red", linestyle=":", label="margin")
plt.plot(X_plt, y_pred - model.epsilon, color="red", linestyle=":")
plt.legend(loc="upper right")

plt.show()
