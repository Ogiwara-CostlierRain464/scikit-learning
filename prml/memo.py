"""
ちょっとしたメモ

arr[:, None, :]

: は「全選択」
Noneは「次元を伸ばす」
に該当

arr.sum(axis=~)

のaxisは、
axis=0 -> 行方向
axis=1 -> 列方向
axis=2以降: データが3次元以上の場合

axis=-1 : 配列のindexと同じように、最後の次元方向を指す
"""