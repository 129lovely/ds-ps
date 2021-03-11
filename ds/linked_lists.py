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

    # insert new node after a particular node
    def insertAfter(self, prev, newNode):
        if prev.next is None:
            self.tail = newNode

        newNode.next = prev.next
        prev.next = newNode

        self.nodeCount += 1
        return True

    # insert new node into a particular index
    def insertAt(self, pos, newNode):
        if pos < 1 or (self.nodeCount + 1) < pos:
            return False

        if pos != 1 and pos == (self.nodeCount + 1):
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)

        return self.insertAfter(prev, newNode)

    # delete a node after a particular node
    def popAfter(self, prev):
        if prev.next is None:
            return None

        curr = prev.next
        if curr.next is None:
            if self.nodeCount == 1:
                self.tail = None
            else:
                self.tail = prev
        prev.next = curr.next

        self.nodeCount -= 1
        return curr.data

    # delete a node by a particular index
    def popAt(self, pos):
        if pos < 1 or self.nodeCount < pos:
            raise IndexError

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    # concatenate two linked lists
    def concat(self, newLinkedList):
        self.tail.next = newLinkedList.head.next
        if newLinkedList.tail is not None:
            self.tail = newLinkedList.tail
        self.nodeCount += newLinkedList.nodeCount