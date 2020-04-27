from math import ceil
from typing import Union
from sys import exit

Key = int
Pointer = str
N = 4
INF = 9999


def count(from_: int, to: int):
    return range(from_, to+1)


class Node(object):
    def __init__(self, size=N-1):
        self.size = size
        self.p_body = [None] * (size+1)
        self.k_body = [INF] * size
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

    # index is key index
    def insert_after(self, index: int, P: Pointer, K: Key):
        for i in count(index + 1, self.size - 1):  # p_index+1以降を一個ずらす
            self.set_p(i + 1, self.p(i))
            self.set_k(i + 1, self.k(i))
        self.set_p(index + 1, P)
        self.set_k(index + 1, K)

    def insert(self, P: Pointer, K: Key):
        index = self.highest_key_index_less_than_or_equal_to_arg(K)
        self.insert_after(index, P, K)

    # [Key]以下で最大、あるいはそれと等しいキーのindexを返す
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
    def has_less_than_n_pointers(self) -> bool:
        #return self.p(self.size) is None
        return self.p(self.size+1) is None

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
        # res += "  parent -> (" + str(self.parent) + ")"
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
        L_.set_p(N, L.p(N))
        L.set_p(N, L_)
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

    if 0 < contain < node.k(1):
        return search_leaf(node.p(1), contain)

    for i in count(2, node.size):
        if node.k(i-1) <= contain < node.k(i):
            return search_leaf(node.p(i), contain)

    if node.k(node.size) < contain:
        return search_leaf(node.p(node.size+1), contain)

    raise ValueError("Should not reach here")


def insert_in_leaf(L: Node, K: Key, P: Pointer):
    if K < L.k(1):
        L.insert_before_p1(P, K)
    else:
        index = L.highest_key_index_less_than_or_equal_to_arg(K)
        # L.insert_after(i, P, K)
        for i in count(index + 1, L.size - 1):  # p_index+1以降を一個ずらす
            L.set_p(i + 1, L.p(i))
            L.set_k(i + 1, L.k(i))
        L.set_p(index + 1, P)
        L.set_k(index + 1, K)


def insert_in_parent(n: Node, K_: Key, N_: Union[Node, Pointer]):
    if n == tree.root:
        R = Node()
        R.set_p(1, n)
        n.parent = R
        R.set_k(1, K_)
        R.set_p(2, N_)
        N_.parent = R
        tree.root = R
        return
    P = n.parent
    if P.has_less_than_n_pointers:
        #P.insert(N_, K_)
        index = P.highest_key_index_less_than_or_equal_to_arg(K_)
        for ki in count(index+1, P.size-1):
            P.set_k(ki+1, P.k(ki))
        for pi in count(index+2, P.size-1):
            P.set_p(pi+1, P.p(pi))
        P.set_k(index+1, K_)
        P.set_p(index+2, N_)
        N_.parent = P
    else:
        T = P.clone()
        T.add_size(1)
        #T.insert(N_, K_)

        index = T.highest_key_index_less_than_or_equal_to_arg(K_)
        for ki in count(index + 1, T.size - 1):
            T.set_k(ki + 1, T.k(ki))
        for pi in count(index + 2, T.size - 1):
            T.set_p(pi + 1, T.p(pi))
        T.set_k(index + 1, K_)
        T.set_p(index + 2, N_)


        N_.parent = T  # link parent
        P.erase_p_and_k()
        P_ = Node()
        for i in count(1, ceil((N+1)/2)-1):
            P.set_p(i, T.p(i))
            P.set_k(i, T.k(i))
        P.set_p(ceil((N+1)/2),T.p(ceil((N+1)/2)))
        K__ = T.k(ceil((N + 1) / 2))
        offset = ceil((N + 1) / 2)
        for i in count(ceil((N + 1) / 2)+1, N):
            P_.set_p(i - offset, T.p(i))
            P_.set_k(i - offset, T.k(i))
        P_.set_p(N+1 - offset, T.p(N+1))
        insert_in_parent(P, K__, P_)


if __name__ == "__main__":
    insert(2, "hi")
    insert(3, "pet")
    insert(4, "dog")
    insert(5, "cat")
    insert(6, "hello")
    insert(9, "jack")
    insert(10, "BAD")
    insert(11, "GOD")
    insert(12, "GO00D")
    insert(13, "W")
    print(tree.root.p(2).p(1).k(2))

