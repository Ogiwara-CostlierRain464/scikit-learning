# About
乱択版クイックソートアルゴリズムにおいて、期待実行時間が
<img src="https://latex.codecogs.com/gif.latex?\Theta&space;(n&space;\lg&space;n&space;)" title="\Theta (n \lg n )" />

であることを示す。

何を書くべき？

最良の分割、均等分割を見た後に平均時評価がそれらとあまり変わらないこと直感的に見る

クイックソートの実行時間は分割が均等か否かに依存し、したがって分割の際にピボットとなる要素
に依存する。分割が均等ならばクイックソートは漸近的にマージソートと同程度に高速だが、
分割が均等でなければ漸近的に挿入ソートと同程度に遅くなることがある。まず、クイックソートの性能を分割が均等である場合と
不均等である場合について直感的に議論する。

# 最悪の分割
クイックソートが最悪の振る舞いをするのは、分割手続きが元の問題を要素数n-1の部分問題と要素数0の部分問題に分割した時である。
実際、漸化式より、

<img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;T(n)&space;&=&space;T(n-1)&space;&plus;&space;T(0)&space;&plus;&space;\Theta(n)&space;\\&space;&=&space;T(n&space;-&space;1)&space;&plus;&space;\Theta(n)&space;\end{align*}" title="\begin{align*} T(n) &= T(n-1) + T(0) + \Theta(n) \\ &= T(n - 1) + \Theta(n) \end{align*}" />

となり、置き換え法より<img src="https://latex.codecogs.com/gif.latex?\Theta(n^2)" title="\Theta(n^2)" />
と解けることがわかる。

したがって、この場合にはクイックソートの最悪実行時間は挿入ソートよりも
よくならず、しかも、<img src="https://latex.codecogs.com/gif.latex?\Theta(n^2)" title="\Theta(n^2)" /> 実行時間が生ずるのは、挿入ソートならば<img src="https://latex.codecogs.com/gif.latex?O(n)" title="O(n)" /> で走る、入力配列がすでに完全にソートされている場合である。



# 最良の分割
最も均等に分割で行われる場合には一方のサイズが<img src="https://latex.codecogs.com/gif.latex?\lfloor&space;n/2&space;\rfloor" title="\lfloor n/2 \rfloor" />で、他方のサイズが<img src="https://latex.codecogs.com/gif.latex?\lceil&space;n/2&space;\rceil&space;-&space;1" title="\lceil n/2 \rceil - 1" /> である。この時、漸化式は

<img src="https://latex.codecogs.com/gif.latex?T(n)&space;=&space;T(\lfloor&space;n/2&space;\rfloor&space;)&space;&plus;&space;T(\lceil&space;n/2&space;\rceil&space;-&space;1&space;)&space;&plus;&space;\Theta&space;(n)" title="T(n) = T(\lfloor n/2 \rfloor ) + T(\lceil n/2 \rceil - 1 ) + \Theta (n)" />

マスター定理を用いて解くので、漸化式の杜撰さが許容され、

<img src="https://latex.codecogs.com/gif.latex?T(n)&space;=&space;2T(&space;n/2&space;)&space;&plus;&space;\Theta&space;(n)" title="T(n) = 2T( n/2 ) + \Theta (n)" />

となり、これを解くと<img src="https://latex.codecogs.com/gif.latex?T(n)&space;=&space;\Theta(n&space;\lg&space;n)" title="T(n) = \Theta(n \lg n)" /> となる。

# 均等分割
直感に反し、クイックソートの平均実行時間は最悪の場合よりも最良の場合に近い。
その理由を理解するキーは、実行時間を表す漸化式に分割の均等化が与える影響を理解することである。

たとえば、分割アルゴリズムが常に9:1の比で問題を分割するとき、漸化式は

<img src="https://latex.codecogs.com/gif.latex?T(n)&space;=&space;T(9n&space;/&space;10)&space;&plus;&space;T(n/10)&space;&plus;&space;cn" title="T(n) = T(9n / 10) + T(n/10) + cn" />

となる。この漸化式に対する再帰木(P145)を見ると、深さ<img src="https://latex.codecogs.com/gif.latex?\log&space;_{10/9}n&space;\in&space;\Theta(\lg&space;n)" title="\log _{10/9}n \in \Theta(\lg n)" />で再帰が終了し、
各レベルのコストは<img src="https://latex.codecogs.com/gif.latex?\Theta&space;(n)" title="\Theta (n)" />
なので、総コストは<img src="https://latex.codecogs.com/gif.latex?\Theta&space;(n&space;\lg&space;n)" title="\Theta (n \lg n)" /> である。直感的にはかなり偏った分割のように見えるが、漸近的にはちょうど真ん中で分割するのと同じとなる。
事実として、分割比が定数である限りは再帰木の深さは<img src="https://latex.codecogs.com/gif.latex?\Theta&space;(&space;\lg&space;n)" title="\Theta ( \lg n)" /> 、各レベルのコストは<img src="https://latex.codecogs.com/gif.latex?\Theta&space;(&space;n)" title="\Theta (n)" />となる。 


# 平均時評価に対する直感
入力される配列の任意の置換が等確率で出現すると仮定する。
ランダムな入力配列上でクイックソートを走らせると、すべてのレベルで分割が同じ比率になるという今までの仮定は満たされそうにない。いくつかの分割は均等に行われるが、いくつかの分割は片寄っている
と考えるのが妥当である。

たとえば、PARTITIONが生成する分割は、80％の場合に9:1よりも均等であり、残りの20%の場合に9:1よりも不均等であることを示す。
この一般的な命題である、「定数α(0 < α ≤ 0.5)において、ランダムな入力配列上のPARTITIONが1-α:αよりも均等な分割を生成する確率が1-2αで近似できる」を証明する。

1-α:αよりも不均等な分割をするには、PARTITIONは長さnの配列に対してαn個の要素より小さい位置か、αn個の要素より大きい位置にピボットを選択する必要がある。各確率はαn/n = αで、両方の確率を合わせると2αとなる。
よって、1-α:αよりも均等な分割をする確率は1-2αである。

この命題により、平均的にはPARTITIONは「良い」分割と「悪い」分割を共に生成する。直感的に理解するため、P146の図のように、悪い分割と良い分割が交互に発生する場合を考える。
まず悪い分割においては<img src="https://latex.codecogs.com/gif.latex?\Theta&space;(n)" title="\Theta (n)" />のコストでサイズが0,n-1の部分配列に分割される。
次に、良い分割においては<img src="https://latex.codecogs.com/gif.latex?\Theta&space;(n&space;-&space;1)" title="\Theta (n - 1)" /> のコストで(n-1)/2 -1と(n-1)/2に分割される。
これは良い分割を一回だけ行った場合と同等の分割結果となり、また分割コストも<img src="https://latex.codecogs.com/gif.latex?\Theta&space;(n)&space;&plus;&space;\Theta&space;(n-1)&space;=&space;\Theta&space;(n)" title="\Theta (n) + \Theta (n-1) = \Theta (n)" />となる。
分割回数2は<img src="https://latex.codecogs.com/gif.latex?\Theta&space;(n)" title="\Theta (n)" />の中に埋もれ、漸近的には最良の分割と同じになることが分かる。


# 乱択版クイックソート
いくつかのアルゴリズムは乱択によってすべての入力に渡って良い期待性能を獲得できる。
入力サイズが十分大きい時、乱択版クイックソートは有名なソーティングアルゴリズムとして広く認知されている。

入力を明示的に置換することでアルゴリズムを乱択化することができるが、ここでは無作為抽出と呼ばれる
別の乱択化手法を用いて解析を行いやすくする。本手法では、`A[r]`をつねにピボットとする代わりに部分配列`A[p..r]`から要素を無作為に抽出し、
それをピボットとして用いる。

# 期待実行時間の解析

QUICK_SORTとRANDOMIZED_QUICK_SORTの相違はピボット要素の選択方法だけにあり、残りは完全に同じである。そこで、ピボット要素が
RANDOMIZED_QUICK_SORTに渡される部分配列から無作為に抽出されるという仮定の元で、QUICK_SORTとPARTITION手続きを議論することで、RANDOMIZED_QUICK_SORTを解析する。

Work in Progress..