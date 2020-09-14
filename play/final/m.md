残念ながら、対策取られていた(Cookie)取得後にダウンロードする必要があったので、手動


アメリカのフライトデータでいいでしょうが
面倒だから、何個かの空港にしぼって、その増減を見てみる

3つ空港えらんでみるか

ロサンゼルス国際(LAX)  : 12892 : 西海岸
サンフランシスコ空港(SFO) : 14771 : 西海岸 
ジョンFケネディ空港(JFK) : 12478 : 東海岸

とりあえず、
1~4月までで各年事に取っていって、
可能ならば推移を見ていく

で、数がわかったところでどうする？


mapでは
reducerではその数を確認

とりあえず平均でもとるか

何が取れるかを考えてみようね



まずは有名な空港に制限して、その航行数を年度で比較
まず2020/1~4までのデータと2019/1~4, 2018/1~4までの比較でどれくらい変化があったのか


```shell script

```


続いて、2018/1,2,3,,,,12 と2019/1,2,3,,,,,12の
普段の月ごとの航行数
月ごとに変化があるのかを調べる
これは各空港ごとに


時間による変化は？
空港ごとに、時間による変化があるかもしれない
例えば夜はどうとか、
2の観察を元に、もっとも航空数が多かった月に限定して(月ごとに傾向変わるかもしれないから)、
これも各空港ごとに
これはLocal timeで良い(夜に出るのが多い、など)(出発と到着で分けよう)




時間の前にin/out数の比較とか？





hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar -files reducer.py,mapper.py -input 2020_test -output 2020_test_out -mapper 'mapper.py' -reducer 'reducer.py'
 
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar -input 2020_test -output 2020_test_out -mapper 'wc -l' -reducer 'wc -l'
