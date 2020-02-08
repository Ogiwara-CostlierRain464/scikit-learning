from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy as np

boston = load_boston()

# 特徴量に平均部屋数(RM)を選択し20行に絞り込み
X = boston.data[:20, [5]]
# 正解に住居価格(MDEV)を設定し、20行に絞り込み
y = boston.target[:20]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=2
)

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

model = LinearRegression()
model2 = SVR(kernel="linear", C=10000.0, epsilon=4.0)

model.fit(X_train_std, y_train)
model2.fit(X_train_std, y_train)

plt.figure(figsize=(8, 4))

X_plt = np.arange(X_train_std.min(), X_train_std.max(), 0.1)[:, None]
y_plt_pred = model.predict(X_plt)
y_plt_pred2 = model2.predict(X_plt)

plt.scatter(X_train_std, y_train, color="blue", label="data")

plt.plot(X_plt, y_plt_pred, color="lime", linestyle="-", label="LinearRegression")
plt.plot(X_plt, y_plt_pred2, color="red", linestyle="-", label="SVR")
plt.plot(X_plt, y_plt_pred2 + model2.epsilon, color="red", linestyle=":", label="margin")
plt.plot(X_plt, y_plt_pred2 - model2.epsilon, color="red", linestyle=":")

plt.ylabel("Price in $1000s [MEDV]")
plt.xlabel("Average number of rooms [RM]")
plt.title("Boston house-prices")
plt.legend(loc="lower right")

plt.show()