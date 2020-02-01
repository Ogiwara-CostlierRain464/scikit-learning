import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

np.random.seed(seed=8)

# 二次元配列に
X = np.random.uniform(0,4,15)[:, np.newaxis]
# 一次元配列に, ノイズの付与
y = np.sin(1/4 * 2 * np.pi * X).ravel() + np.random.normal(0, 0.3, 15)

POLY = PolynomialFeatures(degree=6, include_bias=False)
X_pol = POLY.fit_transform(X)

model = LinearRegression()
model2 = Ridge(alpha=0.1)


# 同じfitが使えるようにPolynomialFeaturesを使っているだけ！
model.fit(X_pol, y)
model2.fit(X_pol, y)

plt.figure(figsize=(8,4))

X_plt = np.arange(0,4,0.1)[:, None]
# 正解
y_true = np.sin(1/4 * 2 * np.pi * X_plt).ravel()

y_pred = model.predict(POLY.transform(X_plt))
y_pred2 = model2.predict(POLY.transform(X_plt))


plt.scatter(X,y,color="blue", label="data")
plt.plot(X_plt, y_true, color="lime", linestyle="-", label="True sin(x)")
plt.plot(X_plt, y_pred, color="red", linestyle="-", label="LinearRegression")
plt.plot(X_plt, y_pred2, color="blue", linestyle="--", label="Ridge")
plt.legend(loc="upper right")

plt.show()