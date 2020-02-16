from algorithm_introduction.helper import *
from math import *


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -INF
    _sum = 0
    for i in down_to(mid, low):
        _sum = _sum + A[i]
        if _sum > left_sum:
            left_sum = _sum
            max_left = i

    right_sum = -INF
    _sum = 0
    for j in count(mid + 1, high):
        _sum = _sum + A[j]
        if _sum > right_sum:
            right_sum = _sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    # 基底
    if high == low:
        return low, high, A[low]
    else:
        # 分割
        mid = floor((low + high) / 2)
        # 統治段階
        (left_low, left_high, left_sum) = \
            find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = \
            find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = \
            find_max_crossing_subarray(A, low, mid, high)
        # 結合
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def full_search(A):
    # compare each collection of (n, m) and find biggest diverge
    max_diverge = 0
    for i in down_to(A.length, 2):
        for j in down_to(i - 1, 1):
            diverge = A[i] - A[j]
            if diverge > max_diverge:
                max_diverge = diverge

    return max_diverge


# arr = AlgorithmArray([13, -3, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
# arr = AlgorithmArray([-5, -9, -78, -4, -3, -3])
arr = AlgorithmArray([13, 3, 5, 6, 8, 3])

# print(find_maximum_subarray(arr, 1, arr.length))
print(full_search(arr))
