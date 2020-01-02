"""
linkedlist.py
linked list implementation in python using linked-node
@author: diptanu sarkar, ds9297@cs.rit.edu
"""
from node import Node


class LinkedList:

    __slots__ = "__front"

    def __init__(self):
        self.__front = None

    def __str__(self):
        output = "LinkedList[ "
        n = self.__front
        if n is None:
            return output + "]"
        while n is not None:
            output += str(n.value) + " "
            n = n.link
        return output + " ]"

    def append(self, value):
        n = self.__front
        new_node = Node(value)
        if n is None:
            self.__front = new_node
        else:
            while n.link is not None:
                n = n.link
            n.link = new_node

    def prepend(self, value):
        self.__front = Node(value, self.__front)

    def size(self):
        return self._size_to_end(self.__front)

    def _size_to_end(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._size_to_end(node.link)

    def start(self):
        return self.__front

    def is_off(self, cursor):
        return cursor is None

    def get_value(self, cursor):
        if self.is_off(cursor):
            raise ValueError
        return cursor.value

    def set_value(self, cursor, new_value):
        if self.is_off(cursor):
            raise ValueError
        cursor.value = new_value

    def next_loc(self, cursor):
        if self.is_off(cursor):
            raise ValueError
        return cursor.link

    def insert(self, cursor, new_value):
        if cursor == self.__front:
            self.prepend(new_value)
        else:
            node = self.__front
            while node is not cursor:
                node = node.link
            node.link = Node(new_value, cursor)

    class _Iter:

        __slots__ = "cursor", "the_list"

        def __next__(self):
            if self.the_list.is_off(self.cursor):
                raise StopIteration
            else:
                result = self.the_list.get_value(self.cursor)
                self.cursor = self.the_list.next_loc(self.cursor)
                return result

    def __iter__(self):
        result = LinkedList._Iter()
        result.the_list = self
        result.cursor = self.start()
        return result


def test():
    l = LinkedList()
    print(l)
    l.append(10)
    print(l)
    l.append(11)
    print(l)
    l.append(12)
    print(l)
    l.prepend(9)
    print(l)


if __name__ == "__main__":
    test()




