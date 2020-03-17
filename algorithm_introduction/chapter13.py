from algorithm_introduction.chapter12 import *
from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 0


class RBNode(Node):
    def __init__(self, key, color: Color, left=None, right=None, p=None):
        super().__init__(key, left, right, p)
        self.color = color


class RBTree(Tree):
    # nil = RBNode(None, Color.BLACK)
    nil = None


def left_rotate(T: RBTree, x: RBNode):
    y = x.right         # yをxの右の子とする
    x.right = y.left    # yの左部分木をxの右部分木にする
    if y.left != T.nil:
        y.left.p = x
    y.p = x.p           # xの親をyにする
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x          # xをyの右の子にする
    x.p = y

# TODO FIX
def right_rotate(T: RBTree, x: RBNode):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x  # xをyの右の子にする
    x.p = y



def rb_sample() -> RBNode:
    _2 = RBNode(2, Color.BLACK)
    _3 = RBNode(3, Color.BLACK, _2)
    _2.p = _3
    _6 = RBNode(6, Color.BLACK)
    _4 = RBNode(4, Color.BLACK, _3, _6)
    _3.p = _4
    _6.p = _4
    _12 = RBNode(12, Color.BLACK)
    _17 = RBNode(17, Color.BLACK)
    _14 = RBNode(14, Color.BLACK, _12, _17)
    _12.p = _14
    _17.p = _14
    _20 = RBNode(20, Color.BLACK)
    _22 = RBNode(22, Color.BLACK, _20)
    _20.p = _22
    _19 = RBNode(19, Color.BLACK, None, _22)
    _22.p = _19
    _18 = RBNode(18, Color.BLACK, _14, _19)
    _14.p = _18
    _19.p = _18
    _9 = RBNode(9, Color.BLACK)
    _11 = RBNode(11, Color.BLACK, _9, _18)
    _9.p = _11
    _18.p = _11
    _7 = RBNode(7, Color.BLACK, _4, _11)
    _4.p = _7
    _11.p = _7

    return _7


if __name__ == "__main__":
    root = rb_sample()
    t = RBTree(root)
    _11 = tree_search(root, 11)
    print(_11.right)
    left_rotate(t, _11)
    _11 = tree_search(root, 11)
    print(_11.right)
    right_rotate(t, _11)
    _11 = tree_search(root, 11)
    print(_11.right)










