"""
node.py
Linked node for implementation of stack, queue and linked-list
author: diptanu sarkar, ds9297@cs.rit.edu
"""


class Node:

    __slots__ = "value", "link"

    def __init__(self, value, link=None):
        """
        constructor of the node
        :param value:
        :param link:
        """
        self.value = value
        self.link = link

    def __str__(self):
        """
        return a string representation of the node
        :return:
        """
        return str(self.value)

    def __repr__(self):
        """
        return a string that, if evaluated, would recreate
        this node and the node to which it is linked.
        :return:
        """
        return "Node( " + repr(self.value) + ", " + repr(self.link) + " )"


def size_to_end(node):
    """
    size of the node
    :param node:
    :return:
    """
    if node is None:
        return 0
    else:
        return 1 + size_to_end(node.link)


def test():
    """
    testing the node implementation
    :return:
    """
    print("Creating 3 nodes")
    nodes = Node(1, Node(1.0, Node("Diptanu")))
    n = nodes
    while n is not None:
        print(n.value)
        n = n.link
    print("\n" + str(size_to_end(nodes)) + " nodes.")
    print(repr(nodes))


if __name__ == "__main__":
    test()