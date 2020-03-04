from algorithm_introduction.helper import *
from math import *


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in count(p, r - 1):
        if A[j] <= x:
            i = i + 1
            swap_arr(A, i, j)

    swap_arr(A, i + 1, r)
    return i + 1


arr = AlgorithmArray([2, 8, 7, 1, 3, 5, 6, 4])
quick_sort(arr, 1, 8)
print(arr)