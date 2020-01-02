"""
bst.py
author: diptanu sarkar, ds9297@rit.edu
implementation of binary search tree
"""

from btnode import BTNode


class BST:

    __slots__ = "root"

    def __init__(self):
        """
        Initialize the tree.
        :return: None
        """
        self.root = None

    def __insert(self, node, val):
        """
        The recursive helper function for inserting a new value into the tree.
        :param val: The value to insert
        :param node: The current node in the tree (BTNode)
        :return: None
        """
        if val < node.val:
            if node.left is None:
                node.left = BTNode(val)
            else:
                self.__insert(node.left, val)
        else:
            if node.right is None:
                node.right = BTNode(val)
            else:
                self.__insert(node.right, val)

    def insert(self, val):
        """
        Insert a new value into the tree
        :param val: The value to insert
        :return: None
        """
        if self.root is None:
            self.root = BTNode(val)
        else:
            self.__insert(self.root, val)

    def __contains__(self, node, val):
        """
        The recursive helper function for checking if a value is in the tree.
        :param val: The value to search for
        :param node: The current node (BTNode)
        :return: True if val is present, False otherwise
        """
        if node is None:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self.__contains__(node.left, val)
        else:
            return self.__contains__(node.right, val)

    def contains(self, val):
        """
        Returns whether a value is in the tree or not.
        :param val: The value to search for
        :return: True if val is present, False otherwise
        """
        # call the recursive helper function with the root node
        return self.__contains__(self.root, val)

    def __size(self, node):
        """
        The recursive helper function for computing the size of a node
        :param node: The current node (BTNode)
        :return: The size of node (int)
        """
        if node is None:
            return 0
        else:
            return 1 + self.__size(node.left) + self.__size(node.right)

    def size(self):
        """
        Return the size of a tree.
        :return: The size of the node (int)
        """
        return self.__size(self.root)

    def __height(self, node):
        """
        The recursive helper function for computing the height of a node
        :param node: The current node (BTNode)
        :return: The height of node (int)
        """
        if node is None:
            return -1
        else:
            return 1 + max(self.__height(node.left), self.__height(node.right))

    def height(self):
        """
        Return the height of a tree.  Recall:
            - The height of an empty tree is -1
            - The height of a tree with one node is 0
            - Otherwise the height is one plus the larger of the heights of
            the left or right children.
        :return: The height (int)
        """
        # just call the recursive helper function with the root node
        return self.__height(self.root)

    def __inorder(self, node):
        """
        The recursive inorder traversal function that builds a string
        representation of the tree.
        :param node: The current node (BTNode)
        :return: A string of the tree, e.g. "1 2 5 9 "
        """
        if node is None:
            return ' '
        else:
            return self.__inorder(node.left) + str(node.val) + \
                   self.__inorder(node.right)

    def __str__(self):
        """
        Return a string representation of the tree.  By default this will
        be a string with the values in order.
        :return:
        """
        # call the recursive helper function with the root node
        return self.__inorder(self.root)


def test():
    """
        Test function for the binary search tree.
        :return: None
        """
    # empty tree
    t0 = BST()
    print('t0:', t0)
    print('t0 size (0):', t0.size())
    print('t0 contains 10 (False)?', t0.contains(10))
    print('t0 height (-1)?', t0.height())

    # single node tree
    t1 = BST()
    t1.insert(10)
    print('t1:', t1)
    print('t1 size (1):', t1.size())
    print('t1 contains 10 (True)?', t1.contains(10))
    print('t1 contains 0 (False)?', t1.contains(0))
    print('t1 height (0)?', t1.height())

    # tree with a parent (20), left child (10) and right child (30)
    t2 = BST()
    for val in (20, 10, 30): t2.insert(val)
    print('t2:', t2)
    print('t2 size (3):', t2.size())
    print('t2 contains 30 (True)?', t2.contains(30))
    print('t2 contains 0 (False)?', t2.contains(0))
    print('t2 height (1)?', t2.height())

    # a larger tree
    t3 = BST()
    for val in (17, 5, 35, 2, 16, 29, 38, 19, 33): t3.insert(val)
    print('t3:', t3)
    print('t3 size (9):', t3.size())
    print('t3 contains 16 (True)?', t3.contains(16))
    print('t3 contains 0 (False)?', t3.contains(0))
    print('t3 height (3)?', t3.height())


if __name__ == "__main__":
    test()
