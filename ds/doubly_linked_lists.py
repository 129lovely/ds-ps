class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # get all nodes in forward
    def traverse(self):
        array = []
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
            array.append(curr.data)
        return array

    # get all nodes in reverse
    def reverse(self):
        array = []
        curr = self.tail
        while curr.prev.prev is not None:
            curr = curr.prev
            array.append(curr.data)
        return array

    # get a node by a particular index
    def getAt(self):
        if pos < 0 or self.nodeCount < pos:
            return None
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    # insert a node after a particular node
    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    # insert a node into a particular index
    def insertAt(self, pos, newNode):
        pass

    def popAfter(self):
        pass

    def popAt(self):
        pass