from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy as np

boston = load_boston()
X = boston.data
y = boston.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=2
)

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

param_grid = [
    {
        "kernel": ["rbf"],
        "C": [1.0, 3.0, 10., 30., 100., 300., 1000.0],
        "gamma": [0.01, 0.03, 0.1, 0.3, 1.0, 3.0],
        "epsilon": [0.01, 0.03, 0.1, 0.3, 1.0, 3.0]
    },
]

model = SVR()
grid_search = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="neg_mean_squared_error",
    verbose=2,
    n_jobs=-1
)
grid_search.fit(X_train_std, y_train)

model_grs = grid_search.best_estimator_
y_train_grs_pred = model_grs.predict(X_train_std)
y_test_grs_pred = model_grs.predict(X_test_std)

print("MSE train: {0}, test: {1}".format(
    mean_squared_error(y_train, y_train_grs_pred),
    mean_squared_error(y_test, y_test_grs_pred),
))
print("Best model is...")
print(grid_search.best_estimator_)

plt.figure(figsize=(8,4))
plt.scatter(
    y_train_grs_pred,
    y_train_grs_pred - y_train,
    c="red",
    marker="o",
    edgecolor="white",
    label="Training data"
)

plt.scatter(
    y_test_grs_pred,
    y_test_grs_pred - y_test,
    c="blue",
    marker="s",
    edgecolor="white",
    label="Test data"
)

plt.xlabel("Predicted values")
plt.ylabel("Residuals")
plt.legend(loc="upper left")
plt.hlines(y=0, xmin=-10, xmax=50, color="black", lw=2)
plt.xlim([-10, 50])
plt.tight_layout()

plt.show()
