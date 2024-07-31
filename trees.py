from typing import Optional

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def to_array(self):
        if self.root is None:
            return []
        queue = [self.root]
        array = []
        while queue:
            node = queue.pop(0)
            array.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return array

    def maxDepth(self, root: Optional[Node] = None) -> int:
        """Given the root of a binary tree, return its depth"""
        if root is None:
            root = self.root
        if not root:
            return 0
        return self._maxDepth(root)

    def _maxDepth(self, node: Optional[Node]) -> int:
        """Helper method to maxDepth"""
        if not node:
            return 0
        return 1 + max(self._maxDepth(node.left), self._maxDepth(node.right))

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(4)
tree.insert(1)
tree.insert(8)
tree.insert(9)
print(tree.maxDepth())  
