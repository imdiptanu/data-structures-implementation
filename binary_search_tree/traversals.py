"""
traversals.py
author: diptanu sarkar, ds9297@cs.rit.edu
implementation of three recursive traversal - preorder, inorder, postorder
"""

from btnode import BTNode


def preorder(node):
    """
    a preorder traversal has a visits parent,
    left and then right.
    :param node: the current node in the traversal (BTNode)
    :return: None
    """
    if node is not None:
        print(node.val, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    """
    a inorder traversal has a visits left,
    parent and then right.
    :param node: the current node in the traversal (BTNode)
    :return: None
    """
    if node is not None:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)


def postorder(node):
    """
    a postorder traversal has a visits left,
    right and then parent.
    :param node: the current node in the traversal (BTNode)
    :return: None
    """
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=" ")


def traverse(node):
    """
    a function that performs all three traversals
    :param node: the root of the tree (BTNode)
    :return: None
    """
    print('Preorder:', end=" ")
    preorder(node)
    print()
    print('inorder:', end=" ")
    inorder(node)
    print()
    print('postorder:', end=" ")
    postorder(node)
    print()


def test_traversal():
    """
    a function to test the traversals over different binary trees.
    :return: None
    """
    # single node
    traverse(BTNode(10))

    # a parent node (20), with left (10) and right (30) children
    traverse(BTNode(20, BTNode(10), BTNode(30)))

    # tree
    traverse(BTNode('A',
            BTNode('B',
                   None,
                   BTNode('D')),
            BTNode('C',
                   BTNode('E',
                          BTNode('G'),
                          None),
                   BTNode('F',
                          BTNode('H'),
                          BTNode('I')))))


if __name__ == "__main__":
    test_traversal()