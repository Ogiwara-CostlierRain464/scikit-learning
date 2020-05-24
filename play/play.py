import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("2019_14204010.csv", encoding="SHIFT-JIS")
df = pd.concat([df, df["日付"].str.split("/", expand=True)], axis=1)
df.rename(columns={0: "YYYY", 1: "MM", 2: "DD"}, inplace=True)
df["日時"] = df["YYYY"] + "-" + df["MM"] + "-" + df["DD"] + " " + (df["時"] - 1).astype(str) + ":00:00"
df["日時"] = pd.to_datetime(df["日時"])
df = df.set_index("日時")

daily = pd.DataFrame(df["PM2.5(ug/m3)"].resample("D").mean())

weather = pd.read_csv("weather.csv", encoding="SHIFT-JIS")
weather["年月日"] = pd.to_datetime(weather["年月日"])
weather = weather.set_index("年月日")

data = daily.join(weather)

# plt.scatter(daily.index, daily["PM2.5(ug/m3)"])
# plt.show()
