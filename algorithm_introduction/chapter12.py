from algorithm_introduction.helper import *


class Node:
    def __init__(self, key, left, right, p):
        self.key = key
        self.left = left
        self.right = right
        self.p = p


def in_order_tree_walk(x: Node):
    if x is not None:
        in_order_tree_walk(x.left)
        print(x.key)
        in_order_tree_walk(x.right)


def tree_search(x: Node, k):
    if (x is None) or (k == x.key):
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def tree_min(x: Node):
    while x.left is not None:
        x = x.left
    return x


def tree_max(x: Node):
    while x.right is not Node:
        x = x.right
    return x


def tree_successor(x: Node):
    if x.right is not Node:
        return tree_min(x.right)
    y = x.p
    while (y is not Node) and (x == y.right):
        x = y
        y = y.p
    return y


if __name__ == "__main__":
    print("HE")

