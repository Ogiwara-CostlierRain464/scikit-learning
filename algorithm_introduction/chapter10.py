from algorithm_introduction.helper import count


class LinkedListElement:
    def __init__(self, prev, key, next):
        self.prev = prev
        self.key = key
        self.next = next

    def __str__(self):
        return "({0}) -> {1}".format(self.key, self.next)

    def __repr__(self):
        return self.__str__()


class LinkedList:
    def __init__(self, head):
        self.head = head

    def __str__(self):
        return "L.head -> {0} ".format(self.head)

    def __repr__(self):
        self.__str__()


def list_search(L: LinkedList, k):
    x = L.head
    while x is not None and x.key != k:
        x = x.next
    return x


def list_insert(L: LinkedList, x: LinkedListElement):
    x.next = L.head
    if L.head is not None:
        L.head.prev = x
    L.head = x
    x.prev = None


def list_delete(L, x):
    if x.prev is not None:
        x.prev.next = x.next
    else:
        L.head = x.next
    if x.next is not None:
        x.next.prev = x.prev


if __name__ == '__main__':
    l = LinkedList(None)
    for i in count(1, 10):
        list_insert(l, LinkedListElement(None, i, None))

    print(l)
