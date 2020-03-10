from algorithm_introduction.helper import *
from algorithm_introduction.chapter10 import *
from math import *


def counting_sort(A: AlgorithmArray, B: AlgorithmArray, k):
    # Cはindexが0から始まる配列であることに注意
    C = [0] * (k+1)
    for j in count(1, A.length):
        C[A[j]] = C[A[j]] + 1
    # C[i]はiと等しい要素の数を表す
    for i in count(1, k):
        C[i] = C[i] + C[i - 1]
    # C[i]はi以下の要素の数を表す
    for j in down_to(A.length, 1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1


# キーを元に計数ソート
def counting_sort_by_key(A: AlgorithmArray[KeyAndItem], B: AlgorithmArray[KeyAndItem], k):
    # Cはindexが0から始まる配列であることに注意
    C = [0] * (k + 1)
    for j in count(1, A.length):
        C[A[j].key] = C[A[j].key] + 1
    # C[i]はiと等しい要素の数を表す
    for i in count(1, k):
        C[i] = C[i] + C[i - 1]
    # C[i]はi以下の要素の数を表す
    for j in down_to(A.length, 1):
        B[C[A[j].key]] = A[j]
        C[A[j].key] = C[A[j].key] - 1


def radix_sort(A, d):
    for i in count(1, d):
        # 安定ソートを用いて第i桁に関して配列Aをソートする
        A_ = make_digit_key_arr(A, i)
        B = AlgorithmArray.empty(A_.length)
        counting_sort_by_key(A_, B, 10)
        A = make_int_arr(B)

    return A


# 数値のdigit桁目を取得する
def take_digit(num, digit):
    for _ in count(1, digit):
        div = floor(num / 10)
        rem = num % 10
        num = div
    return rem


# 数値配列を元に、digit桁目をキーとする配列を返す
def make_digit_key_arr(A: AlgorithmArray[int], digit) -> AlgorithmArray[KeyAndItem]:
    tmp = list(map(lambda e_: KeyAndItem(
        take_digit(e_, digit), e_
    ), A.body))
    return AlgorithmArray(tmp)


# キー配列を元に、数値配列を返す
def make_int_arr(A: AlgorithmArray[KeyAndItem]) -> AlgorithmArray[int]:
    tmp = list(map(lambda e_: e_.item, A.body))
    return AlgorithmArray(tmp)


def bucket_sort(A):
    n = A.length
    # Bはindexが0から始まることに注意
    B = [0] * n
    for i in count(0, n - 1):
        B[i] = LinkedList(None)
    for i in count(1, n):
        list_insert(B[floor(n * A[i])] , LinkedListElement(None, A[i], None))
    # WIP
    print(B)


arr = AlgorithmArray([.78, .17, .39, .26, .72, .94, .21, .12, .23, .68])
bucket_sort(arr)