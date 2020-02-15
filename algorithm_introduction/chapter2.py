from math import floor

from algorithm_introduction.helper import AlgorithmArray, INF, count


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


def marge_sort(A, p, r):
    if p < r:
        q = floor((p + r) / 2)
        marge_sort(A, p, q)
        marge_sort(A, q + 1, r)
        merge(A, p, q, r)


arr = AlgorithmArray([5, 2, 4, 6, 1, 3])

marge_sort(arr, 1, arr.length)

print(arr)
