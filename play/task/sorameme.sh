# 2019/05分のデータを取得
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