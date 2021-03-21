class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        left = self.left.size() if self.left else 0
        right = self.right.size() if self.right else 0
        return left + right + 1


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def size(self):
        if self.root:  # if not empty tree
            return self.root.size()
        else:
            return 0

    def depth(self):
        pass

    def traversal(self):
        pass
