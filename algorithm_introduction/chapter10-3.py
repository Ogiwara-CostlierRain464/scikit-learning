from algorithm_introduction.helper import *

#  単一配列表現を用いて、Allocate objectとFree objectを表現
A = AlgorithmArray([
    None, None, None,
    1, None, 7,
    8, 4, None,
    None, 1, None
])

L = 7
free = 10


def offset_next(index):
    return index + 1


def offset_prev(index):
    return index - 1


def allocate_object():
    global free
    global A

    if free is None:
        raise ValueError("No more memory")
    else:
        x = free
        free = A[offset_next(x)]
        return x


def free_object(x):
    global free
    global A

    A[offset_next(x)] = free
    free = x


if __name__ == "__main__":
    print(free_object(4))
    print(free_object(7))
    print(L, free, A)
