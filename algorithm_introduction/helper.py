class AlgorithmArray:
    def __init__(self, body):
        self._body = body

    def __getitem__(self, item):
        return self._body[item - 1]

    def __setitem__(self, key, value):
        self._body[key - 1] = value

    @property
    def length(self):
        return len(self._body)

    def __str__(self):
        return str(self._body)

    @staticmethod
    def empty(size):
        return AlgorithmArray([None] * size)


def count(begin, to):
    return range(begin, to+1)


def down_to(begin, to):
    return range(begin, to-1,-1)


def swap(a, b):
    return b, a


INF = 99999


