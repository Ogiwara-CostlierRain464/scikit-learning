from math import floor

from algorithm_introduction.helper import AlgorithmArray, INF, count, down_to, swap


def insertion_sort(a):
    for j in range(2, a.length + 1):
        key = a[j]
        i = j - 1
        while i > 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1

        a[i + 1] = key


def linear_search(a, v):
    for j in range(1, a.length + 1):
        if a[j] == v:
            return j

    return None


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = AlgorithmArray.empty(n1 + 1)
    R = AlgorithmArray.empty(n2 + 1)
    for i in count(1, n1):
        L[i] = A[p + i - 1]
    for j in count(1, n2):
        R[j] = A[q + j]
    L[n1 + 1] = INF
    R[n2 + 1] = INF
    i = 1
    j = 1
    for k in count(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


# 「番兵」を用いないMERGEアルゴリズム
def merge2(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = AlgorithmArray.empty(n1)
    R = AlgorithmArray.empty(n2)
    for i in count(1, n1):
        L[i] = A[p + i - 1]
    for j in count(1, n2):
        R[j] = A[q + j]
    i = 1
    j = 1
    for k in count(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
            # ここがLが書き戻されたタイミング
            # ここで、Lが全て書き戻されたかチェックすればよい
            if i > L.length:
                for jj in count(j, R.length):
                    k = k + 1
                    A[k] = R[jj]

                return
        else:
            A[k] = R[j]
            j = j + 1
            # ここがRが書き戻されたタイミング
            if j > R.length:
                for ii in count(i, L.length):
                    k = k + 1
                    A[k] = L[ii]

                return


def marge_sort(A, p, r):
    if p < r:
        q = floor((p + r) / 2)
        marge_sort(A, p, q)
        marge_sort(A, q + 1, r)
        merge2(A, p, q, r)


def bubble_sort(A):
    for i in count(1, A.length - 1):
        print("{0} i:{1} ".format(A, i))
        for j in down_to(A.length, i + 1):
            # print("{0} i:{1} j:{2}".format(A, i, j))
            if A[j] < A[j - 1]:
                (A[j], A[j - 1]) = swap(A[j], A[j - 1])


arr = AlgorithmArray([5, 2, 4, 1145, 6, 1, 3, 5, 89])

# marge_sort(arr, 1, arr.length)
bubble_sort(arr)

print(arr)
