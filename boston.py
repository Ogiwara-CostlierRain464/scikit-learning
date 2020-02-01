from sklearn.datasets import load_boston
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

boston = load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)

df["MEDV"] = boston.target
x = df.RM.to_frame()
y = df.MEDV

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

lr = LinearRegression()

lr.fit(x_train, y_train)

print(lr.predict(x_test))
