import random
from typing import TypeVar, Generic


class KeyAndItem:
    def __init__(self, key, item):
        self.key = key
        self.item = item

    def __str__(self):
        return "({0}: {1})".format(self.key, self.item)

    def __repr__(self):
        return self.__str__()


T = TypeVar('T', int, KeyAndItem)


class AlgorithmArray(Generic[T]):
    def __init__(self, body):
        self.body = body

    def __getitem__(self, item) -> T:
        return self.body[item - 1]

    def __setitem__(self, key, value: T):
        self.body[key - 1] = value

    @property
    def length(self):
        return len(self.body)

    def __str__(self):
        return str(self.body)

    def __repr__(self):
        return self.__str__()

    # work as same as arr * 5
    def __mul__(self, other):
        assert isinstance(other, int)
        times = other
        arr = []
        for _ in count(1, other):
            copy = self.body.copy()
            arr.append(AlgorithmArray(copy))
        return AlgorithmArray(arr)

    @staticmethod
    def empty(size):
        return AlgorithmArray([None] * size)

    @staticmethod
    def empty_n_m(n, m):
        return AlgorithmArray.empty(m) * n


def count(begin, to):
    return range(begin, to + 1)


def down_to(begin, to):
    return range(begin, to - 1, -1)


def swap(a, b):
    return b, a


def swap_arr(arr, index1, index2):
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp


def int_random(from_, to):
    return random.randrange(from_, to + 1)


INF = 99999

if __name__ == "__main__":
    for i in down_to(3,1):
        print(i)
