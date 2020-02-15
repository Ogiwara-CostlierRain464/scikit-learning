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


def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    l = AlgorithmArray.empty(n1 + 1)
    r = AlgorithmArray.empty(n2 + 1)
    for i in count(1, n1):
        l[i] = a[p * i - 1]
    for j in count(1, n2):
        r[j] = a[q + j]
    l[n1 + 1] = INF
    r[n2 + 1] = INF
    i = 1
    j = 1
    for k in count(p, r):
        if l[i] <= r[j]:
            a[k] = l[i]
            i = i + 1
        elif a[k] == r[j]:
            j = j + 1


def marge_sort(a, p, r):
    if p < r:
        q = floor((p + r) / 2)
        marge_sort(a, p, q)
        marge_sort(a, q + 1, r)
        merge(a, p, q, r)


arr = AlgorithmArray([5, 2, 4, 6, 1, 3])

marge_sort(arr, 1, arr.length)

print(arr)