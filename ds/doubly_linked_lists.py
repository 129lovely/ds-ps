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
    def getAt(self, pos):
        if pos < 0 or self.nodeCount < pos:
            return None

        i = 0
        if pos > self.nodeCount // 2:
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
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

    # insert a node before a particular node
    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    # insert a node into a particular index
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    # delete a node after a particular node
    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    # delete a node before a particular node
    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    # delete a note by a particular index
    def popAt(self, pos):
        if pos < 1 or self.nodeCount < pos:
            raise IndexError
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    # concatenate two linked lists
    def concat(self, newDoublyLinkedList):
        link_prev = self.tail.prev
        link_next = newDoublyLinkedList.head.next
        link_prev.next = link_next
        link_next.prev = link_prev
        self.tail = newDoublyLinkedList.tail
        self.nodeCount += newDoublyLinkedList.nodeCount