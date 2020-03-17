from typing import Union, Optional

from algorithm_introduction.helper import *


class Node:
    def __init__(self, key, left=None, right=None, p=None):
        self.key = key
        self.left = left
        self.right = right
        self.p = p

    def __str__(self):
        return "Node({0})".format(self.key)

    def __repr__(self):
        return self.__str__()


class Tree:
    def __init__(self, root: Node):
        self.root = root


def in_order_tree_walk(x: Node):
    if x is not None:
        in_order_tree_walk(x.left)
        print(x.key)
        in_order_tree_walk(x.right)


def tree_search(x: Node, k) -> Optional[Node]:
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


def tree_min_rec(x: Node):
    if x.left is None:
        return x
    else:
        return tree_min_rec(x.left)


def tree_max(x: Node):
    while x.right is not None:
        x = x.right
    return x


def tree_max_rec(x: Node):
    if x.right is None:
        return x
    else:
        return tree_max_rec(x.right)


def tree_successor(x: Node):
    if x.right is not None:
        return tree_min(x.right)
    y = x.p
    while (y is not None) and (x == y.right):
        x = y
        y = y.p
    return y


def tree_predecessor(x: Node):
    if x.left is not None:
        return tree_max(x.left)
    y = x.p
    while (y is not None) and (x == y.left):
        x = y
        y = y.p
    return y


def tree_insert(T: Tree, z: Node):
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def tree_insert_rec(x: Node, z: Node):
    if z.key > x.key:
        if x.right is None:
            x.right = z
            x.right.p = x
        else:
            tree_insert_rec(x.right, z)
    else:
        if x.left is None:
            x.left = z
            x.left.p = x
        else:
            tree_insert_rec(x.left, z)


def sample() -> Node:
    two = Node(2, None, None, None)
    four = Node(4, None, None, None)
    three = Node(3, two, four, None)
    two.p = three
    four.p = three

    nine = Node(9, None, None, None)
    thirteen = Node(13, nine, None, None)
    nine.p = thirteen
    seven = Node(7, None, thirteen, None)
    thirteen.p = seven
    six = Node(6, three, seven, None)
    three.p = six
    seven.p = six

    seventeen = Node(17, None, None, None)
    twenty = Node(20, None, None, None)
    eighteen = Node(18, seventeen, twenty, None)
    seventeen.p = eighteen
    twenty.p = eighteen

    fifteen = Node(15, six, eighteen, None)
    six.p = fifteen
    eighteen.p = fifteen

    return fifteen


if __name__ == "__main__":
    root = sample()

    t = Tree(root)
    # in_order_tree_walk(t.root)
    tree_insert_rec(root, Node(19))
    in_order_tree_walk(t.root)
    _19 = tree_search(root, 19)
    print(_19.p)
    print(_19.left)
    print(_19.right)

