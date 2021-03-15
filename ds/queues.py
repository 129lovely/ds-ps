from doubly_linked_lists import Node
from doubly_linked_lists import DoublyLinkedList


class ArrayQueue:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class DoublyLinkedListQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.nodeCount

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        newNode = Node(item)
        self.data.insertAt(self.size() + 1, newNode)

    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data