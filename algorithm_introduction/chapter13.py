from enum import Enum
from typing import Union

from algorithm_introduction.helper import *


class Color(Enum):
    RED = 1
    BLACK = 0


class RBTree:
    def __init__(self, root):
        self.root = root


class RBNode:
    def __init__(self, key, color: Color, left=None, right=None, p=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.p = p

    def __str__(self):
        return "RBNode({0})".format(self.key)

    def __repr__(self):
        return self.__str__()


# p, left, right, keyは任意の要素を取れる
TreeNIL = RBNode(key=INF, color=Color.BLACK)


def make_node(key, color: Color = Color.BLACK):
    return RBNode(key=key, color=color, left=TreeNIL, right=TreeNIL, p=TreeNIL)


RBNode.apply = make_node


def in_order_tree_walk(x: RBNode):
    if x != TreeNIL:
        in_order_tree_walk(x.left)
        print(x.key)
        in_order_tree_walk(x.right)


def tree_search(x: RBNode, k):
    if (x == TreeNIL) or (k == x.key):
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def tree_min(x: RBNode):
    while x.left != TreeNIL:
        x = x.left
    return x


def tree_max(x: RBNode):
    while x.right != TreeNIL:
        x = x.right
    return x


def tree_successor(x: RBNode):
    if x.right != TreeNIL:
        return tree_min(x.right)
    y = x.p
    while (y != TreeNIL) and (x == y.right):
        x = y
        y = y.p
    return y


def tree_predecessor(x: RBNode):
    if x.left != TreeNIL:
        return tree_max(x.left)
    y = x.p
    while (y != TreeNIL) and (x == y.left):
        x = y
        y = y.p
    return y


# x.right != TreeNIL, T.root.p == TreeNILを仮定
def left_rotate(T: RBTree, x: RBNode):
    y = x.right         # yをxの右の子とする
    x.right = y.left    # yの左部分木をxの右部分木にする
    if y.left != TreeNIL:
        y.left.p = x
    y.p = x.p           # xの親をyにする
    if x.p == TreeNIL:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x          # xをyの右の子にする
    x.p = y


# x.left != TreeNIL, T.root.p == TreeNILを仮定
def right_rotate(T: RBTree, x: RBNode):
    y = x.left
    x.left = y.right
    if y.right != TreeNIL:
        y.right.p = x
    y.p = x.p
    if x.p == TreeNIL:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x  # xをyの右の子にする
    x.p = y


def rb_insert_fixup(T: RBTree, z: RBNode):
    while z.p.color == Color.RED:
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == Color.RED:
                z.p.color = Color.BLACK
                y.color = Color.BLACK
                z.p.p.color = Color.RED
                z = z.p.p
            elif z == z.p.right:
                z = z.p
                left_rotate(T, z)
            z.p.color = Color.BLACK
            z.p.p.color = Color.RED
            right_rotate(T, z.p.p)
        else:
            y = z.p.p.left
            if y.color == Color.RED:
                z.p.color = Color.BLACK
                y.color = Color.BLACK
                z.p.p.color = Color.RED
                z = z.p.p
            elif z == z.p.left:
                z = z.p
                right_rotate(T, z)
            z.p.color = Color.BLACK
            z.p.p.color = Color.RED
            left_rotate(T, z.p.p)
    T.root.color = Color.BLACK


def rb_insert(T: RBTree, z: RBNode):
    # 12章のtree_insertと同じ
    y = TreeNIL
    x = T.root
    while x != TreeNIL:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == TreeNIL:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = TreeNIL
    z.right = TreeNIL
    z.color = Color.RED
    rb_insert_fixup(T, z)


def rb_sample() -> RBNode:
    _2 = RBNode.apply(2)
    _3 = RBNode.apply(3)

    _3.left = _2; _2.p = _3

    _6 = RBNode.apply(6)
    _4 = RBNode.apply(4)

    _4.left = _3; _3.p = _4
    _4.right = _6; _6.p = _4

    _12 = RBNode.apply(12)
    _17 = RBNode.apply(17)
    _14 = RBNode.apply(14)

    _14.left = _12; _12.p = _14
    _14.right = _17; _17.p = _14

    _20 = RBNode.apply(20)
    _22 = RBNode.apply(22)

    _22.left = _20; _20.p = _22

    _19 = RBNode.apply(19)

    _19.right = _22; _22.p = _19

    _18 = RBNode.apply(18)

    _18.left = _14; _14.p = _18
    _18.right = _19; _19.p = _18

    _9 = RBNode.apply(9)
    _11 = RBNode.apply(11)

    _11.left = _9; _9.p = _11
    _11.right = _18; _18.p = _11

    _7 = RBNode.apply(7)

    _7.left = _4; _4.p = _7
    _7.right = _11; _11.p = _7

    return _7


if __name__ == "__main__":
    root = rb_sample()
    t = RBTree(root)

    z = RBNode.apply(1)

    rb_insert(t, z)
    rb_insert(t, RBNode.apply(8))

    in_order_tree_walk(root)












