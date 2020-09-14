# 大規模データ処理法 最終課題
荻原 湧志 #71970013

# Abstract
United States Department of Transportationにて公開されている航空データ[1]
をもとに、アメリカ国内の空港のうち、ロサンゼルス国際空港、サンフランシスコ空港、ジョンFケネディ空港
の三つの空港において、以下のようなデータ分析を行なった。

- コロナの影響によるアメリカ国内の航空量の変化はどの程度あったのか
- 月ごと、季節ごとのアメリカ国内の航空量の変化はどの程度あるのか
- 時間帯ごとのアメリカ国内の航空量の変化はどの程度あるのか


# 導入
コロナによる影響を測る一つの指針として、交通量の増減が考えられる。このレポートでは、
United States Department of Transportationにて公開されている航空データ[1]
を元に、2019年度と比べて2020年度のアメリカ国内の航空量にはどの程度の変化があったのかを調べた。
また、2019年度の航空データについて、月ごと・季節ごとの航空量の変化はどの程度のものなのか、
また時間帯ごとの航空量の変化はどの程度あるのかを分析した。

傾向を観やすくするために、アメリカ国内全空港の総計をとるのではなく、アメリカでも有名な
ロサンゼルス国際空港、サンフランシスコ空港、ジョンFケネディ空港の三つの空港に絞って分析を行なった。

このデータを分析の対象として選んだ理由としては、無効値やデータ形式のばらつきが少ないためデータの前処理がしやすく、
またより多くのデータを収集でき、MapReduceアルゴリズムの良い演習になると考えたからである、

# 方法・結果
まずは[1]のリンクから、航空データのダウンロードを行なった。

- YEAR: 航空した年度
- MONTH: 航空した月
- FL_DATE: 航空した日付
- ORIGIN_AIRPORT_ID: 出発した空港のID
- DEST_AIRPORT_ID: 到着した空港のID
- DEP_TIME: 出発時間(ローカル時間)
- ARR_TIME: 到着時間(ローカル時間)

の7つのカラムを含むようにフォームを記入し、2019/01 ~ 2020/04までの各月のデータをCSV形式でダウンロードした。
Botによるダウンロードを試みたが、対策されていたので手動で全てダウンロードし、`data`フォルダに`(年度)(月).csv`の形式で各CSVを保存した。
合計、9,565,278レコードであった。

ダウンロードしたデータのうち、Airport IDがロサンゼルス国際空港(LAX)、サンフランシスコ空港(SFO)、ジョンFケネディ空港(JFK)
に該当するものについての調査を行なった。空港名とAirport IDの対応付けは[2]で確認し、
ロサンゼルス国際空港は`12892`、サンフランシスコ空港は`14771`、ジョンFケネディ空港は`12478`に対応することが
分かった。

MapReduceアルゴリズムの処理については、Hadoop上よりローカルマシンでのシェルスクリプト実行の方が高速に処理できたため、
ローカルマシン上で処理をした。

ローカルマシンのスペックは、
- プロセッサ: 2.3 GHz Dual-Core Intel Core i5
- メモリ: 16 GB 2133 MHz LPDDR3

である。また、各MapReduce処理の実行時間も記載した。

## コロナによる航空量の増減

まず、コロナによる航空量の増減の変化を確認をした。
各空港において、1~4月の航空機の到着・出発量の集計を取り、それを2019年と
2020年で比較した。

```python
#!/usr/bin/python3
import sys


AIRPORT_LIST = ["12892", "14771", "12478"]


def is_looking_airport(array):
    if str(array[3]) in AIRPORT_LIST:
        return str(array[3])
    if str(array[4]) in AIRPORT_LIST:
        return str(array[4])
    return None


for line in sys.stdin:
    line = line.strip()
    arr = line.split(",")
    if len(arr) != 8:
        continue
    airport = is_looking_airport(arr)
    if airport is None:
        continue
    print(airport)
```
コード: mapper.py


```python
#!/usr/bin/python3
import sys

# LAX, SFO, JFK
AIRPORT_LIST = ["12892", "14771", "12478"]

lax_count = 0
sfo_count = 0
jfk_count = 0

for line in sys.stdin:
    line = line.strip()
    if line == AIRPORT_LIST[0]:
        lax_count += 1
    if line == AIRPORT_LIST[1]:
        sfo_count += 1
    if line == AIRPORT_LIST[2]:
        jfk_count += 1

print("LAX", "\t", lax_count)
print("SFO", "\t", sfo_count)
print("JFK", "\t", jfk_count)
```
コード: reducer.py

```shell script
cat data/20200[1-4].csv | ./mapper.py | sort | ./reducer.py
```
スクリプト1: 2020年度の1~4月の各空港の航空量の出力

```shell script
cat data/20190[1-4].csv | ./mapper.py | sort | ./reducer.py
```
スクリプト2: 2019年度の1~4月の各空港の航空量の出力


Map操作ではAirport IDが上記の三つの空港に該当するものに対してフィルタリングをし、
Reduce操作ではAirport IDをkeyとしてその数を集計した。

スクリプト1の結果
```
LAX      113060
SFO      84644
JFK      61665
```

スクリプト2の結果
```
LAX      132565
SFO      100973
JFK      77192
```

各スクリプトとも、約3.7秒で処理が完了した。

これより、3つのどの空港においても、コロナによる1~4月での航空量の
減少は15000程度であると考えられる。

## 2019年度の航空データについて、月ごと・季節ごとの航空量の変化

次に、2019年度の月ごとの航空量の変化を確認した。
各空港において、各月の航空機の到着・出発量の集計を取った。

```python
#!/usr/bin/python3
import sys


AIRPORT_LIST = ["12892", "14771", "12478"]


def is_looking_airport(array):
    if str(array[3]) in AIRPORT_LIST:
        return str(array[3])
    if str(array[4]) in AIRPORT_LIST:
        return str(array[4])
    return None


for line in sys.stdin:
    line = line.strip()
    arr = line.split(",")
    if len(arr) != 8:
        continue
    airport = is_looking_airport(arr)
    if airport is None:
        continue
    print(airport + "\t" + arr[1])
```
コード: mapper.py

```python
#!/usr/bin/python3
import sys

# LAX, SFO, JFK
AIRPORT_LIST = ["12892", "14771", "12478"]

lax_count = [0]*12
sfo_count = [0]*12
jfk_count = [0]*12

for line in sys.stdin:
    arr = line.strip().split("\t")
    assert len(arr) == 2

    print(arr)

    if arr[0] == AIRPORT_LIST[0]:
        lax_count[int(arr[1]) - 1] += 1
    if arr[0] == AIRPORT_LIST[1]:
        sfo_count[int(arr[1]) - 1] += 1
    if arr[0] == AIRPORT_LIST[2]:
        jfk_count[int(arr[1]) - 1] += 1

print("LAX", "\t", lax_count)
print("SFO", "\t", sfo_count)
print("JFK", "\t", jfk_count)
```
コード: reducer.py

```shell script
cat data/2019*.csv | ./mapper.py | sort | ./reducer.py
```


Map操作ではAirport IDが上記の三つの空港に該当するものに対してフィルタリングをし、(空港ID, 月)のペアを作り、
Reduce操作では各空港ごとに、月ごとの集計を取った。

結果
```
LAX      [33618, 30473, 35168, 33306, 34287, 35511, 37494, 37203, 33353, 34186, 32812, 35119]
SFO      [25477, 22861, 26795, 25840, 26834, 27753, 29162, 31380, 24928, 26924, 25343, 26337]
JFK      [19275, 17726, 20629, 19562, 20082, 19834, 20400, 20601, 18864, 19328, 18265, 19226]
```

![](LAX2019.png)
グラフ: LAXの2019年の月ごとの航空量

![](SFO2019.png)
グラフ: SFOの2019年の月ごとの航空量

![](JFK2019.png)
グラフ: JFKの2019年の月ごとの航空量

スクリプト処理は約12秒で完了した。

グラフより、どの空港においても、
- 2,11月は谷となっており、航空量が大きく落ち込む
- 1,3,8,12月といったホリデーシーズンに航空量が増える

と考えられる。


## 時間帯ごとの航空量の変化

最後に、時間帯ごとの航空量の変化がどの程度か調査した。
各空港について、前の調査より8月が最も航空量が多かったことが分かったので、その月に対して
3時間おきに区切って航空機の到着・出発量の集計を取った。


以下のプログラムでは、3時間ごとの区切りを、

0~2時を`0`, 4~6時を`1`, 7~9時を`2`, 10~12時を`3`,
13~15時を`4`, 16~18時を`5`, 19~21時を`6`, 22~24時を`7`

という風にラベル付けした。

```python
#!/usr/bin/python3
import sys

AIRPORT_LIST = ["12892", "14771", "12478"]


def is_looking_airport(id):
    return str(id) if str(id) in AIRPORT_LIST else None


def time_to_label(time: str):
    time = time.replace('"', '')
    if len(time) != 4:
        return None
    month = int(time[0:2])
    label = month // 3
    return label if label <= 7 else 7


for line in sys.stdin:
    line = line.strip()
    arr = line.split(",")

    if arr[0] == '"YEAR"':  # Ommit first line
        continue

    if len(arr) != 8:  # Not valid record
        continue
    if int(arr[1]) != 8:  # Not looking month
        continue

    origin_looking_port = is_looking_airport(arr[3])
    dest_looking_port = is_looking_airport(arr[4])
    if origin_looking_port is not None:
        label = time_to_label(arr[5])
        if label is not None:
            print(origin_looking_port + "\t" + str(label))
    if dest_looking_port is not None:
        label = time_to_label(arr[6])
        if label is not None:
            print(dest_looking_port + "\t" + str(label))
```
コード: mapper.py

```python
#!/usr/bin/python3
import sys

# LAX, SFO, JFK
AIRPORT_LIST = ["12892", "14771", "12478"]

lax_count = [0]*8
sfo_count = [0]*8
jfk_count = [0]*8

for line in sys.stdin:
    arr = line.strip().split("\t")
    assert len(arr) == 2

    if arr[0] == AIRPORT_LIST[0]:
        lax_count[int(arr[1])] += 1
    if arr[0] == AIRPORT_LIST[1]:
        sfo_count[int(arr[1])] += 1
    if arr[0] == AIRPORT_LIST[2]:
        jfk_count[int(arr[1])] += 1

print("LAX", "\t", lax_count)
print("SFO", "\t", sfo_count)
print("JFK", "\t", jfk_count)
```
コード: reducer.py

```shell script
cat data/201908.csv | ./mapper.py | sort | ./reducer.py
```

Map操作ではAirport IDが上記の三つの空港に該当するものに対してフィルタリングをし、(空港ID, 時間ラベル)のペアを作り、
Reduce操作では各空港ごとに、時間ごとの集計を取った。



結果
```
LAX      [1261, 885, 6290, 7182, 5806, 5972, 6022, 5810]
SFO      [1221, 661, 4563, 6342, 5259, 5110, 4954, 4931]
JFK      [810, 750, 3972, 3138, 3369, 3564, 3356, 2768]
```

![](LAX08.png)
グラフ: 2019/08のLAXの時間帯ごとの航空量

![](SFO08.png)
グラフ: 2019/08のSFOの時間帯ごとの航空量

![](JFK08.png)
グラフ: 2019/08のJFKの時間帯ごとの航空量

スクリプト処理は約1.5秒で完了した。

グラフより、LAXとSFOにおいては時間ラベル3(10~12時)にてピークを迎えるのに
対し、JFKにおいては時間ラベル2(7~9時)にてピークを迎えることがわかる。

これは、LAXとSFOは西海岸に位置するのに対し、JFKは東海岸に位置することから
起因していると考えられる。

また、時間ラベル0と7で航空量が連続していないことも興味深い。ナイトフライトは
ある程度の航空量があるが、深夜帯(0~6時)は航空量が急に少なくなる、と捉えられる。

# 考察
- コロナによる航空量の現象は11%ほどであり、確実に影響を与えていると考えられる。
- 月ごと、時間帯ごとの航空量の変化は、人間社会の傾向を大きく反映し、またそれを元に調節されたものであると考えられる。
- 約1000万件のデータを扱ったが、MapReduceアルゴリズムとして処理を落とし込んだことで、Unixパイプライン処理による並列化の恩恵を受けることができ、Hadoopを使わずとも手元のマシンで高速に処理することができたと考えられる。

# 参考文献
1. United States Department of Transportation: Bereau of Transportation Statistics 2020/07/22 閲覧 (https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236)
2. United States Department of Transportation: Airport List 2020/07/22 閲覧 (https://www.transtats.bts.gov/NewAirportList.asp?xpage=airports.asp&flag=FACTS)