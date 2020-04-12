from algorithm_introduction.helper import *
from math import *


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def randomized_quick_sort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quick_sort(A, p, q - 1)
        randomized_quick_sort(A, q + 1, r)


def quick_sort2(arr, p, r):
    if p < r:
        q = partition2(arr, p, r)
        quick_sort2(arr, p, q - 1)
        quick_sort2(arr, q + q, r)


def partition2(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            # swap
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    # swap
    tmp = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = tmp
    return i + 1


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in count(p, r - 1):
        if A[j] <= x:
            i = i + 1
            swap_arr(A, i, j)

    swap_arr(A, i + 1, r)
    return i + 1


def randomized_partition(A, p, r):
    i = int_random(p, r)
    swap_arr(A, r, i)
    return partition(A, p, r)


if __name__ == "__main__":
    num = [3, 5, 1, 2, 4]
    quick_sort2(num, 0, 4)

    for e in num[::-1]:  # traverse the iterable
        print(e)
