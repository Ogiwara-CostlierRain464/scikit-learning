from math import ceil
from typing import Union

Key = int
Pointer = str
N = 4
INF = 9999


def count(from_: int, to: int):
    return range(from_, to+1)


class Node(object):
    def __init__(self, size=N-1):
        self.size = size
        self.p_body = [None] * size
        self.k_body = [INF] * size
        self.next = None
        self.parent = None

    def p(self, index: int):
        return self.p_body[index - 1]

    def set_p(self, index: int, pointer):
        self.p_body[index - 1] = pointer

    def k(self, index: int) -> Key:
        return self.k_body[index - 1]

    def set_k(self, index: int, key: Key):
        self.k_body[index - 1] = key

    def insert_before_p1(self, P: Pointer, K: Key):
        for i in count(1, self.size - 1):  # p1以降を一個ずらす
            self.set_p(i + 1, self.p(i))
            self.set_k(i + 1, self.k(i))
        self.set_p(1, P)
        self.set_k(1, K)

    def insert_after(self, index: int, P: Pointer, K: Key):
        for i in count(index + 1, self.size - 1):  # p_index+1以降を一個ずらす
            self.set_p(i + 1, self.p(i))
            self.set_k(i + 1, self.k(i))
        self.set_p(index + 1, P)
        self.set_k(index + 1, K)

    def insert(self, P: Pointer, K: Key):
        index = self.highest_key_index_less_than_or_equal_to_arg(K)
        self.insert_after(index, P, K)

    # [Key]以下で最大、あるいはそれと等しいキーのを返す
    def highest_key_index_less_than_or_equal_to_arg(self, K: Key):
        prev = 1
        for i in count(1, self.size):
            if K >= self.k(i) > prev:
                prev = i
        return prev

    @property
    def is_not_full(self):
        return self.k(self.size) == INF

    @property
    def is_less_than_n_pointers(self) -> bool:
        return self.p(self.size) is None

    @property
    def smallest_key(self):
        return self.k(1)

    @property
    def is_leaf(self) -> bool:
        return isinstance(self.p(1), Pointer)

    def erase_p_and_k(self):
        self.p_body = [None] * self.size
        self.k_body = [INF] * self.size

    def clone(self):
        copy = Node()
        copy.p_body = self.p_body.copy()
        copy.k_body = self.k_body.copy()
        copy.next = self.next
        copy.parent = self.parent
        copy.size = self.size
        return copy

    def add_size(self, additional_size):
        for _ in count(1, additional_size):
            self.p_body.append(None)
            self.k_body.append(INF)
        self.size += additional_size

    def __str__(self):
        res = ""
        for i in count(1, self.size):
            res += "(" + str(self.p(i)) + ")"
            res += " " + str(self.k(i)) + " "
        res += "  next -> (" + str(self.next) + ")"
        return res

    def __repr__(self):
        return self.__str__()


class Tree:
    def __init__(self):
        self.root = None

    @property
    def is_empty(self) -> bool:
        return self.root is None


tree = Tree()


def insert(K: Key, P: Pointer):
    if tree.is_empty:
        L = Node()
        tree.root = L
    else:
        L = search_leaf(tree.root, K)
    if L.is_not_full:
        insert_in_leaf(L, K, P)
    else:
        L_ = Node()
        T = L.clone()
        T.add_size(1)
        insert_in_leaf(T, K, P)
        L_.next = L.next
        L.next = L_
        L.erase_p_and_k()
        for i in count(1, ceil(N / 2)):
            L.set_p(i, T.p(i))
            L.set_k(i, T.k(i))
        for i in count(ceil(N / 2) + 1, N):
            offset = ceil(N / 2)
            L_.set_p(i - offset, T.p(i))
            L_.set_k(i - offset, T.k(i))
        K_ = L_.smallest_key
        insert_in_parent(L, K_, L_)


def search_leaf(node: Node, contain: Key):
    if node.is_leaf:
        return node

    for i in count(1, node.size):
        if contain < node.k(i):
            return search_leaf(node.p(i), contain)

    raise ValueError("Should not reach here")


def insert_in_leaf(L: Node, K: Key, P: Pointer):
    if K < L.k(1):
        L.insert_before_p1(P, K)
    else:
        i = L.highest_key_index_less_than_or_equal_to_arg(K)
        L.insert_after(i, P, K)


def insert_in_parent(n: Node, K_: Key, N_: Union[Node, Pointer]):
    if n == tree.root:
        R = Node()
        R.set_p(0, n)
        R.set_k(0, K_)
        R.set_p(1, N_)
        tree.root = R
        return
    P = n.parent
    if P.is_less_than_n_pointers:
        P.insert(N_, K_)
        N_.parent = P
    else:
        T = P.clone()
        T.add_size(1)
        T.insert(N_, K_)
        N_.parent = T  # link parent
        P.erase_p_and_k()
        P_ = Node()
        for i in count(1, ceil((N+1)/2)):
            P.set_p(i, T.p(i))
        K__ = T.k(ceil((N + 1) / 2))
        for i in count(ceil((N + 1) / 2)+1, N):
            P_.set_p(i, T.p(i))
        P_.next = T.next
        insert_in_parent(P, K__, P_)


if __name__ == "__main__":
    insert(2, "hi")
    insert(3, "pet")
    insert(4, "pet")
    insert(5, "pet")
    print(tree.root)

