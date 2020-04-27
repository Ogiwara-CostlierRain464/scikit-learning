# tree.root -> ROOT
# L: Leaf: key count: n
# Set L'.Pn = L.Pn で本来のLの次のLeaf(L2とす)をコピー
# Set L.Pn = L' で L -> L' の関係を作る
# L -> L' -> L2 の配置になるね
# insert in parentは「insertによって子供のleafが倍増したから、それを親にも通知」
# 当然、insert in parentにてparentのnの数が超えるかもしれないので、parentを上にpopするかもね
# KはKey Pointerは実際に何かのデータを指し示している
# Kは属性なし
# Pも属性なし
# L.P1, L.K1,  ... L.Pn-1, L.Kn-1, Pn
# Tはただのコピー
from math import ceil
from typing import Tuple

Key = int
Pointer = str
N = 4
INF = 99999


class Node(object):
    def __init__(self):
        self.body = [None] * (N * 2)
        self.next = None
        self.parent = None  # you have to link child and parent

    def p(self, index) -> Pointer:
        return self.body[2 * index - 2]

    def set_p(self, index, pointer: Pointer):
        self.body[2 * index - 2] = pointer

    def k(self, index: int) -> Key:
        return self.body[2 * index - 1]

    def set_k(self, index: int, key: Key):
        self.body[2 * index - 1] = key

    @property
    def highest_key(self) -> Tuple[Key, int]:
        """
        :return: tuple of highest key and it's index(max is n-1)
        """
        prev = 0
        for n in range(1, N):
            k_n = self.k(n)
            if k_n == INF:
                return prev, n - 1
            prev = k_n
        return prev, N-1

    @property
    def smallest_key(self) -> Key:
        return self.k(1)

    @property
    def is_not_full(self):
        _, index = self.highest_key
        return index < N-1

    def erase_without_next(self):
        self.body = [INF] * (N * 2)

    def clone(self):
        copy = Node()
        copy.body = self.body.copy()
        copy.next = self.next
        return copy


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
        # Find the leaf node L that should contain key value K
        pass
    if L.is_not_full:
        insert_in_leaf(L, K, P)
    else:
        L_ = Node()
        T = L.clone()
        insert_in_leaf(T, K, P)
        L_.next = L.next
        L.next = L_
        L.erase_without_next()
        for i in range(1, ceil(N/2)+1):
            L.set_p(i, T.p(i))
            L.set_k(i, T.k(i))
        for i in range(ceil(N/2)+1, N):
            offset = ceil(N/2)
            L_.set_p(i - offset, T.p(i))
            L_.set_k(i - offset, T.k(i))
        K_ = L_.smallest_key
        insert_in_parent(L, K_, L_)


def insert_in_leaf(L: Node, K: Key, P: Pointer):
    if K < L.k(1):
        # insert P,K into L just before L.P1
        pass
    else:
        # Some
        pass


def insert_in_parent(n: Node, K_: Key, N_: Node): # N' must be typo, N -> n, N' is now Node
    if tree.root == n:
        pass


if __name__ == "__main__":
    l = Node()
    l.set_k(1,1)
    l.set_k(2,3)
    #l.set_k(3,6)
    print(l.is_not_full)

