from doubly_linked_lists import Node, DoublyLinkedList


class PriorityQueue:
    def __init__(self, x):
        self.queue = DoublyLinkedList()

    def size():
        return self.queue.nodeCount

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next.next and x <= curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.size())

    def peek(self):
        return self.queue.getAt(self.size()).data