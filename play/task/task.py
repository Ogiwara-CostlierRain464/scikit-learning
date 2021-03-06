from enum import Enum
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# weather.csv は辻堂の2019/5 の時間ごとの天気
# "soramame.csv" は同じ場所、時間の大気汚染データ
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from skrvm import RVR


class Label(Enum):
    Temp = "気温(℃)"
    Light = "日照時間(時間)"
    Rain = "降水量(mm)"
    Wind = "風速(m/s)"
    PM2_5 = "PM2.5(ug/m3)"


# weather.csvの整形
df = pd.read_csv("weather.csv", encoding="SHIFT-JIS")
df["年月日時"] = pd.to_datetime(df["年月日時"])
df = df.set_index("年月日時")

# soramame.csvの整形
df2 = pd.read_csv("soramame.csv", encoding="SHIFT-JIS")
df2 = pd.concat([df2, df2["日付"].str.split("/", expand=True)], axis=1)
df2.rename(columns={0: "YYYY", 1: "MM", 2: "DD"}, inplace=True)
df2["日時"] = df2["YYYY"] + "-" + df2["MM"] + "-" + df2["DD"] + " " + (df2["時"] - 1).astype(str) + ":00:00"
df2["日時"] = pd.to_datetime(df2["日時"])
df2 = df2.set_index("日時")

# 大気汚染データと天候データをまとめる
data = df.join(df2)

# 風向、蒸気圧、雲量は使えなさそうだ
data = data.drop(["風向", "蒸気圧(hPa)", "雲量(10分比)"], axis=1)

# 日照時間は日がそもそも出てないとnanになっているので0に
data[Label.Light.value].fillna(0, inplace=True)

# PM2.5はnanは平均値で置き換え
data[Label.PM2_5.value].fillna(data[Label.PM2_5.value].mean(), inplace=True)

# まずは基本的なデータの分布をみてみる
plt.plot(data[Label.PM2_5.value], c="red")
plt.plot(data[Label.Wind.value], c="blue")
plt.plot(data[Label.Rain.value], c="green")
plt.show()

# さて、気温と日照時間についてはあきらかにトゲのあるデータになっており扱いにくそうだ
# とりあえず降水量と風速に絞ってみる
# ここで、風速は明らかに気温や日照時間に影響されている(依存している)ので、風速のみで説明できそうだ

# さて、このデータに対し機械学習をかけて見よう

X = data[[Label.Rain.value, Label.Wind.value]]
y = data[Label.PM2_5.value]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=2
)

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

# Random Forest, RVR, Lassoで機械学習
model1 = RandomForestRegressor(bootstrap=True, criterion="mse")
model2 = RVR(kernel="rbf")
model3 = Lasso(alpha=0.1)

model1.fit(X_train_std, y_train)
model2.fit(X_train_std, y_train)
model3.fit(X_train_std, y_train)

y_train_pred = model1.predict(X_train_std)
y_test_pred = model1.predict(X_test_std)

print("Random Forest MSE train: {0}, test: {1}".format(
    mean_squared_error(y_train, y_train_pred),
    mean_squared_error(y_test, y_test_pred)
))

y_train_pred = model2.predict(X_train_std)
y_test_pred = model2.predict(X_test_std)

print("RVR MSE train: {0}, test: {1}".format(
    mean_squared_error(y_train, y_train_pred),
    mean_squared_error(y_test, y_test_pred)
))

y_train_pred = model3.predict(X_train_std)
y_test_pred = model3.predict(X_test_std)

print("Lasso MSE train: {0}, test: {1}".format(
    mean_squared_error(y_train, y_train_pred),
    mean_squared_error(y_test, y_test_pred)
))

# 相関係数を確認
print(data.corr())

data["SPM(mg/m3)"].fillna(0, inplace=True)
X = data["SPM(mg/m3)"]
y = data[Label.PM2_5.value]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=2
)

model = RandomForestRegressor(bootstrap=True, criterion="mse")
model.fit(X_train[:, np.newaxis], y_train)

y_train_pred = model.predict(X_train[:, np.newaxis])
y_test_pred = model.predict(X_test[:, np.newaxis])

print("Random forest MSE train: {0}, test: {1}".format(
    mean_squared_error(y_train, y_train_pred),
    mean_squared_error(y_test, y_test_pred)
))


