class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    # get a node by a particular index
    # TODO
    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    # get all nodes
    def traverse(self):
        array = []
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            array.append(curr.data)
        return array

    # insert new node into a particular index
    def insertAt(self, pos, newNode):
        if pos < 1 or (self.nodeCount + 1) < pos:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == (self.nodeCount + 1):
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == (self.nodeCount + 1):
            self.tail = newNode

        self.nodeCount += 1
        return True

    # delete a node by a particular index
    def popAt(self, pos):
        if pos < 1 or self.nodeCount < pos:
            raise IndexError

        curr = None
        prev = self.getAt(pos - 1)
        if prev is not None:
            curr = prev.next
            prev.next = curr.next
        else:
            curr = self.head
            self.head = curr.next

        if pos == self.nodeCount:
            self.tail = prev

        self.nodeCount -= 1

        return curr.data

    # concatenate two linked lists
    def concat(self, newLinkedList):
        self.tail.next = newLinkedList.head
        if self.tail:
            self.tail = newLinkedList.tail
        self.nodeCount += newLinkedList.nodeCount