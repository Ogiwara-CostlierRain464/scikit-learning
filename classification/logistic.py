import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

df_wine = pd.read_csv("wine.csv", header=None)
df_wine.columns = ["Class label", "Alcohol", "malic acid", "Ash", "Alcalinity of ash",
                   "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
                   "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"
                   ]

# 特徴量に色とプロリンの量を選択
X = df_wine.iloc[:, [10, 13]].values
# ラベルが0から始まるように設定
y = df_wine.iloc[:, 0].values - 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

model = LogisticRegression(
    max_iter=100,
    multi_class="ovr",
    solver="liblinear",
    C=1.0,
    penalty="l2",
    l1_ratio=None,
    random_state=0
)

model.fit(X_train_std, y_train)

y_test_pred = model.predict(X_test_std)
ac_score = accuracy_score(y_test, y_test_pred)

# print("正解率: {0}".format(ac_score))

plt.figure(figsize=(8, 4))
plot_decision_regions(X_test_std, y_test, model)
plt.show()
