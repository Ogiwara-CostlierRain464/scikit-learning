from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR, LinearSVC
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("wine.csv", header=None)
df.columns = [
    "Class label", "Alcohol", "malic acid", "Ash", "Alcalinity of ash",
    "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
    "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"
]
df = df[44:71]

# 特徴量に色(10列)とプロリンの量(13列)を選択
X = df.iloc[:, [10, 13]].values
# 正解ラベルの設定(ラベルはゼロから開始するよう-1にする)
y = df.iloc[:, 0].values - 1

sc = StandardScaler()
X_std = sc.fit_transform(X)

model = LinearSVC(loss="hinge", C=1000.0, multi_class="ovr", penalty="l2", random_state=0)
model.fit(X_std, y)

X_plt = np.linspace(-3, 3, 200)[:, None]

w = model.coef_[0]
b = model.intercept_[0]
decision_boundary = -w[0] / w[1] * X_plt - b / w[1]

margin = 1 / w[1]
margin_up = decision_boundary + margin
margin_down = decision_boundary - margin

plt.figure(figsize=(8, 4))
plt.plot(X_plt, decision_boundary, linestyle="-", color="black", label="LinearSVC")
plt.plot(X_plt, margin_up, linestyle=":", color="red", label="margin")
plt.plot(X_plt, margin_down, linestyle=":", color="blue", label="margin")
plt.scatter(X_std[:, 0][y == 1], X_std[:, 1][y == 1], c="r", marker="x", label="1")
plt.scatter(X_std[:, 0][y == 0], X_std[:, 1][y == 0], c="b", marker="s", label="0")
plt.legend(loc="best")

plt.show()
