from algorithm_introduction.helper import *
from math import *
import numpy as np


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


def linear_search(A):
    m = -INF
    low_m = high_m = None
    m_r = 0
    low_r = 1
    for i in count(1, A.length):
        m_r += A[i]
        if m_r > m:
            low_m = low_r
            high_m = i
            m = m_r
        if m_r < 0:
            m_r = 0
            low_r = i + 1

    return low_m, high_m, m


def strassen(A: np.ndarray, B: np.ndarray):
    A11, A12, A21, A22 = separate_quantum(A)
    B11, B12, B21, B22 = separate_quantum(B)
    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12
    P1 = A11.dot(S1)
    P2 = S2.dot(B22)
    P3 = S3.dot(B11)
    P4 = A22.dot(S4)
    P5 = S5.dot(S6)
    P6 = S7.dot(S8)
    P7 = S9.dot(S10)
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7
    return C11, C12, C21, C22


def separate_quantum(A: np.ndarray) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    x = A.shape[0]
    y = A.shape[1]
    assert x == y
    n = int(x / 2)
    A11 = A[0:n, 0:n]
    A12 = A[0:n, n:]
    A21 = A[n:, 0:n]
    A22 = A[n:, n:]
    return A11, A12, A21, A22


arr = AlgorithmArray([13, -3, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
# arr = AlgorithmArray([-5, -9, -78, -4, -3, -3])
# arr = AlgorithmArray([13, 3, 5, 6, 8, 3])

A = np.array(
    [[1, 3],
     [7, 5]]
)
B = np.array(
    [[6, 8],
     [4, 2]]
)

print(A.dot(B))
print(strassen(A, B))

# print(find_maximum_subarray(arr, 1, arr.length))
# print(full_search(arr))
# print(linear_search(arr))
