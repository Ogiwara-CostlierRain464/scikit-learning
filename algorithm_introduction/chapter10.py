from algorithm_introduction.helper import *


class Queue(AlgorithmArray):
    def __init__(self, size: int):
        super().__init__([0] * size)
        self.head = 1
        self.tail = 1


def enqueue(Q: Queue, x):
    if Q.head == Q.tail + 1 or (Q.head == 1 and Q.tail == Q.length):
        raise ValueError("Overflow")
    Q[Q.tail] = x
    if Q.tail == Q.length:
        Q.tail = 1
    else:
        Q.tail = Q.tail + 1


def dequeue(Q: Queue):
    if Q.tail == Q.head:
        raise ValueError("Underflow")
    x = Q[Q.head]
    if Q.head == Q.length:
        Q.head = 1
    else:
        Q.head = Q.head + 1
    return x


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
        return self.__str__()


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
    pass

