# 大気汚染データと天候データのデータ分析
荻原湧志 71970013

# 目的
大気汚染データ及び天候データを用いて、PM2.5の測定量と天候との関係を見出す。

# 方法
PM2.5の測定量と、天候との関係を見出すために、そらまめ君[1]及び気象庁の気象データ[2]のデータを分析した。
PM2.5の測定量が多くなると言われている5月のデータをもとに、教師あり機械学習を用いた分析を行なった。
インターネットの接続状況が不安定だったため、Google Colaboratoryではなく手元のローカルマシンで分析を行なった。


# 手順
## そらまめ君[1]のデータをダウンロード

まずは以下のコードでデータをダウンロードし、`soramame.csv`として保存した。
```shell script
wget http://soramame.taiki.go.jp/DownLoad/201905/201905_00.zip

# ダウンロードしたデータを展開
mkdir data
for f in 201905_00.zip; do
  unzip $f -d data
done

mkdir csv
for f in data/*.zip; do
  unzip $f -d csv
done

# 2019/05での神奈川県(県番号14)の辻堂(観測局番号14204010)
# のデータをsoramame.csvとして保存
cp csv/14/201905_14_14204010.csv soramame.csv
```

## 気象庁の気象データ[2]をダウンロード
気象データは[2]をもとに、2019/05/01から2019/05/31の期間での
辻堂の1時間ごとの気温、日照時間、降水量、風向き、風速、蒸気圧、雲量のデータをダウンロードした
このデータはこのままでは扱えないので、1,2,3,5行目を消し、4行目の二つ目の「風速(m/s)」を「風向」に変えた。

## データの整形

データの整形は以下のコードを用いて行なった。

```python
import pandas as pd
import matplotlib.pyplot as plt

# soramame.csvの整形
df2 = pd.read_csv("soramame.csv", encoding="SHIFT-JIS")
df2 = pd.concat([df2, df2["日付"].str.split("/", expand=True)], axis=1)
df2.rename(columns={0: "YYYY", 1: "MM", 2: "DD"}, inplace=True)
df2["日時"] = df2["YYYY"] + "-" + df2["MM"] + "-" + df2["DD"] + " " + (df2["時"] - 1).astype(str) + ":00:00"
df2["日時"] = pd.to_datetime(df2["日時"])
df2 = df2.set_index("日時")

# weather.csvの整形
df = pd.read_csv("weather.csv", encoding="SHIFT-JIS")
df["年月日時"] = pd.to_datetime(df["年月日時"])
df = df.set_index("年月日時")

# 大気汚染データと天候データをまとめる
data = df.join(df2)

# 風向、蒸気圧、雲量は使えなさそうだ
data = data.drop(["風向", "蒸気圧(hPa)", "雲量(10分比)"], axis=1)

# 日照時間は日がそもそも出てないとnanになっているので0に
data["日照時間(時間)"].fillna(0, inplace=True)

# PM2.5はnanは平均値で置き換え
data["PM2.5(ug/m3)"].fillna(data["PM2.5(ug/m3)"].mean(), inplace=True)
```

とりあえずPythonのコードを載せるのは整形まで、それ以降はだるい



## データの分析

まずはそらまめくんと気象庁の気象データをダウンロード
そらまめくんはコードへのリンクを貼る

# わかったこと

# 感想

# 参考文献
1. そらまめ君 http://soramame.taiki.go.jp/ 2020/5/25閲覧
2. 気象庁 気象データ http://www.data.jma.go.jp/gmd/risk/obsdl/index.php 2020/5/25閲覧