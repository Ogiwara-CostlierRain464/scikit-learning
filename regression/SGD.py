from sklearn.datasets import load_boston
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

boston = load_boston()
X = boston.data
y = boston.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

model = SGDRegressor(
    loss="squared_loss",
    max_iter=100,
    eta0=0.01,
    learning_rate="constant",
    alpha=1e-09,
    penalty="l1",
    l1_ratio=0,
    random_state=0
)

model.fit(X_train_std, y_train)

y_train_pred = model.predict(X_train_std)
y_test_pred = model.predict(X_test_std)

print("MSE train: {0}, test: {1}".format(
    mean_squared_error(y_train, y_train_pred),
    mean_squared_error(y_test, y_test_pred)
))