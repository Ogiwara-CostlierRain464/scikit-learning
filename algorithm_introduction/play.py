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


arr = AlgorithmArray([5, 2, 4, 6, 1, 3])

print(linear_search(arr, 999))
