"""
queue.py
Stack implementation in python using linked-node
@author: diptanu sarkar, ds9297@cs.rit.edu
"""
from node import Node


class Queue:

    __slots__ = "front", "back"

    def __init__(self):
        self.front = None
        self.back = None

    def __str__(self):
        output = "Queue["
        n = self.front
        while n is not None:
            output += " " + str(n.value)
            n = n.link
        return output + " ]"

    def is_empty(self):
        return self.front is None

    def peek(self):
        assert not self.is_empty(), "peek on empty queue"
        return str(self.front)

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
        else:
            self.back.link = node
        self.back = node

    def dequeue(self):
        assert not self.is_empty(), "peek on empty queue"
        self.front = self.front.link
        if self.front is None:
            self.back = None

    insert = enqueue
    remove = dequeue


def test():
    s = Queue()
    print(s)
    for value in 1, 2, 3:
        s.enqueue(value)
        print(s)
    print("Dequeueing:", s.peek())
    s.dequeue()
    print(s)
    for value in 15, 16:
        s.insert(value)
        print(s)
    print("Removing:", s.peek())
    s.remove()
    print(s)
    while not s.is_empty():
        print("Dequeueing:", s.peek())
        s.dequeue()
        print(s)
    print("Trying one too many dequeues... ", end="")
    try:
        s.dequeue()
        print("Problem: it succeeded!")
    except Exception as e:
        print("Exception was '" + str(e) + "'")


if __name__ == "__main__":
    test()