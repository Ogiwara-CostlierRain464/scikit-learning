import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mlxtend.plotting import plot_decision_regions
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC, SVC

# XORのデータを生成する(x=正,y=正)=0, (x=正,y=負)=1

X_xor = np.array([[1.6, -0.6], [0.9, -2.4], [-0.3, -1.0]])
y_xor = np.array([1, 1, 0])

X_train, y_train = X_xor, y_xor

model = SVC(kernel="rbf", gamma=1.0, C=100, random_state=0)
# model = SVC(kernel="linear", gamma=1.0, C=100, random_state=0)

model.fit(X_train, y_train)

plt.figure(figsize=(8,4))
plot_decision_regions(X_train, y_train, model)
plt.show()
