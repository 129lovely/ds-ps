from doubly_linked_lists import Node
from doubly_linked_lists import DoublyLinkedList


class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


class DoublyLinkedListStack:
    def __init__(self):
        self.data = DoublyLinkedListStack()

    def size(self):
        return self.data.nodeCount

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass