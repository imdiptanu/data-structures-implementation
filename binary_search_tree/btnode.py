"""
btnode.py
author: diptanu sarkar, ds9297@cs.rit.edu
binary tree node for tree data structure implementation using pyhton3
"""


class BTNode:

    __slots__ = "val", "left", "right"

    def __init__(self, val, left=None, right=None):
        """
        constructor for BTNode
        :param val:
        :param left:
        :param right:
        """
        self.val = val
        self.left = left
        self.right = right


def test():
    """
    test the binary search tree node
    :return:
    """
    left = BTNode(2)
    right = BTNode(3)
    parent = BTNode(1, left, right)
    print("Parent: " + str(parent.val))
    print("Left: " + str(parent.left.val))
    print("Right: " + str(parent.right.val))


if __name__ == "__main__":
    test()