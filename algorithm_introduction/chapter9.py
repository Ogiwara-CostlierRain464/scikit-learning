from algorithm_introduction.helper import *
from algorithm_introduction.chapter7 import *
from math import *


# A[p..r]のi番目に小さい要素を返す
def randomized_select(A: AlgorithmArray, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


if __name__ == "__main__":
    arr = AlgorithmArray([3, 4, 1, 5, 6])
    # print(randomized_select(arr, 1, arr.length, 1))
    print(partition(arr, 1, arr.length))
    p = 1
    r = 5
    i = 1
    q = 5
    k = q - p + 1  # 5

    print((q + 1, arr.length)) # select(A, 6, 5, 1 - 5)
    # これを呼び出すと、
