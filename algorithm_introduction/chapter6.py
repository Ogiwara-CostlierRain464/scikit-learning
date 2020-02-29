from math import *

from algorithm_introduction.helper import *


class HeapArray(AlgorithmArray):
    def __init__(self, body):
        super().__init__(body)
        self.heap_size = self.length


def parent(i):
    return floor(i / 2)


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        swap_arr(A, i, largest)
        max_heapify(A, largest)


def build_max_heap(A):
    A.heap_size = A.length
    for i in down_to(floor(A.length / 2), 1):
        max_heapify(A, i)


def min_heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= A.heap_size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        swap_arr(A, i, smallest)
        min_heapify(A, smallest)


def heapsort(A):
    build_max_heap(A)
    for i in down_to(A.length, 2):
        swap_arr(A, 1, i)
        A.heap_size = A.heap_size - 1
        max_heapify(A, 1)


# MAXIMUM: 最大のキーを持つ要素を返す
def heap_maximum(A):
    return A[1]


# 最大のキーを持つ要素を削除し、その要素を返す
def heap_extract_max(A):
    if A.heap_size < 1:
        raise ValueError("HEAP UNDER FLOW")
    max = A[1]
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    max_heapify(A, 1)
    return max


# 要素iのキーの値を新しいキー値keyに変更する。
def heap_increase_key(A, i, key):
    if key < A[i]:
        raise ValueError("Newer key must be smaller than current key.")
    A[i] = key
    while i > 1 and A[parent(i)] < A[i]:
        swap_arr(A, i, parent(i))
        i = parent(i)


# 要素keyを挿入する
def max_heap_insert(A, key):
    A.heap_size = A.heap_size + 1
    A[A.heap_size] = -INF
    heap_increase_key(A, A.heap_size, key)



arr = HeapArray([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])

heapsort(arr)

print(arr)
