import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn import datasets
from sklearn.svm import SVC

wine = datasets.load_wine()

# 特徴量に色(9列)とプロリンの量(12列)を選択
X = wine.data[:, [9, 12]]
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

model = SVC(
    kernel="rbf",
    gamma=1.5,
    C=100.0,
    decision_function_shape="ovr",
    random_state=0
)

model.fit(X_train_std, y_train)

y_test_std = model.predict(X_test_std)
ac_score = accuracy_score(y_test, y_test_std)
print("正解率 :{:2.2%}".format(ac_score))

plt.figure(figsize=(8,4))
# plot_decision_regions(X_train_std, y_train, model)
plot_decision_regions(X_test_std, y_test, model)
plt.show()