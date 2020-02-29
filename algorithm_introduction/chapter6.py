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
    pass


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


arr = HeapArray([1, 9, 3, 4, 5, 6, 7, 8, 2])

min_heapify(arr, 2)

print(arr)
