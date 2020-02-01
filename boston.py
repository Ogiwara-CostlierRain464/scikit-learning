from sklearn.datasets import load_boston
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import matplotlib.pyplot as plt
import numpy as np

np.random.normal()

df = pd.read_csv("housing.csv", header=None, sep="\s+")

df.columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX",
              "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO",
              "B", "LSTAT", "MEDV"]

# 全ての特徴量
X = df.iloc[:, 0:13].values
# 正解(目的変数)に住宅価格を設定
y = df["MEDV"].values

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=0)

POLY = PolynomialFeatures(degree=2, include_bias=False)

X_train_pol = POLY.fit_transform(X_train)
X_test_pol = POLY.transform(X_test)

sc = StandardScaler()

X_train_std = sc.fit_transform(X_train_pol)
X_test_std = sc.transform(X_test_pol)

model = LinearRegression()
model.fit(X_train_std, y_train)

y_train_pred = model.predict(X_train_std)
y_test_pred = model.predict(X_test_std)

print("MSE train: {0}, test: {1}".format(
    mean_squared_error(y_train, y_train_pred),
    mean_squared_error(y_test, y_test_pred)
))