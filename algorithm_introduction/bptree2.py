from math import ceil
from typing import Tuple, Union, Optional

# Key is for non-left node helper index
# Pointerはleftの要素が指し示しているなにか、ではない
# Leafと中間Nodeの差を作っているのは、p1が何も指していない場合
# 川島先生のスライド通り、LeafとNodeを同一視することに
# 判定方法としては、p1がNodeかPointerかで判別

Key = int
Pointer = str
N = 4
INF = 9999
INIT_KEY = None


class Node(object):
    def __init__(self):
        self.p_body = [None] * (N - 1)
        self.k_body = [INIT_KEY] * (N - 1)
        self.next = None
        self.parent = None

    def p(self, index: int) -> Optional:
        # return Union[Node, Pointer]
        return self.p_body[index - 1]

    def set_p(self, index: int, pointer):
        self.p_body[index - 1] = pointer

    def k(self, index: int) -> Optional[Key]:
        return self.k_body[index - 1]

    def set_k(self, index: int, key: Key):
        self.k_body[index - 1] = key

    def insert_before_p1(self, P: Pointer, K: Key):
        for i in range(1, N - 1):  # p1以降を一個ずらす
            self.set_p(i + 1, self.p(i))
            self.set_k(i + 1, self.k(i))
        self.set_p(1, P)
        self.set_k(1, K)

    def insert_after(self, index: int, P: Pointer, K: Key):
        for i in range(index + 1, N - 1):  # p_index+1以降を一個ずらす
            self.set_p(i + 1, self.p(i))
            self.set_k(i + 1, self.k(i))
        self.set_p(index + 1, P)
        self.set_k(index + 1, K)

    def insert(self, P: Pointer, K: Key):
        index = self.highest_index_less_than_or_equal(K)
        self.insert_after(index, P, K)

    # 要素が空の場合はNoneを返す
    def highest_index_less_than_or_equal(self, K: Key) -> Optional:
        if self.k(1) == INIT_KEY:
            return None

        prev = 1
        for i in range(1, N):
            if self.k(i) == INIT_KEY:
                return prev
            if self.k(i) >= K:
                return prev
            prev = self.k(i)
        return prev

    # 空の場合はNoneを返す
    @property
    def highest_key(self) -> Optional[Tuple[Key, int]]:
        if self.k(1) is INIT_KEY:
            return None

        prev = 0
        for n in range(1, N):
            k_n = self.k(n)
            if k_n is INIT_KEY:
                return prev, n - 1
            prev = k_n
        return prev, N - 1

    @property
    def smallest_key(self) -> Optional[Key]:
        return self.k(1)

    @property
    def is_not_full(self) -> bool:
        _, index = self.highest_key
        return index < N - 1

    @property
    def is_less_than_n_pointers(self) -> bool:
        # return self.next is None
        return self.p(N - 1) is None

    @property
    def is_leaf(self) -> bool:
        return isinstance(self.p(1), Pointer)

    def erase_without_next(self):
        self.p_body = [None] * (N - 1)
        self.k_body = [INIT_KEY] * (N - 1)

    def clone(self):
        copy = Node()
        copy.p_body = self.p_body.copy()
        copy.k_body = self.k_body.copy()
        copy.next = self.next
        return copy

    def __str__(self):
        res = ""
        for i in range(1, N):
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
        insert_in_leaf(T, K, P)
        L_.next = L.next
        L.next = L_
        L.erase_without_next()
        for i in range(1, ceil(N / 2) + 1):
            L.set_p(i, T.p(i))
            L.set_k(i, T.k(i))
        for i in range(ceil(N / 2) + 1, N):
            offset = ceil(N / 2)
            L_.set_p(i - offset, T.p(i))
            L_.set_k(i - offset, T.k(i))
        K_ = L_.smallest_key
        insert_in_parent(L, K_, L_)


def search_leaf(node: Node, contain: Key) -> Optional[Node]:
    if node.is_leaf:
        return node

    for i in range(1, N):
        if contain < node.k(i):
            return search_leaf(node.p(i), contain)

    return None


def insert_in_leaf(L: Node, K: Key, P: Pointer):
    if K < L.k(1):
        L.insert_before_p1(P, K)
    else:
        i = L.highest_index_less_than_or_equal(K)
        L.insert_after(i, P, K)


# rename N -> n
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
        N_.parent = P  # link parent
    else:
        T = P.clone()
        T.insert(N_, K_)
        N_.parent = T  # link parent
        P.erase_without_next()
        P_ = Node()
        for i in range(1, ceil((N + 1) / 2) + 1):
            P.set_p(i, T.p(i))
            P.set_k(i, T.k(i))
        K__ = T.k(ceil((N + 1) / 2))
        for i in range(ceil((N + 1) / 2) + 1, N):
            P_.set_p(i, T.p(i))
            P_.set_k(i, T.k(i))
        insert_in_parent(P, K__, P_)


if __name__ == "__main__":
    insert(2, "hi")
    insert(3, "pet")
    print(tree.root)
