from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """You are given the root of a binary tree root. Invert the binary tree and return its root."""
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [root, 1]
        result = 0
        
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.result = max(self.result, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.result

solution = Solution()    
root_values = [3,9,20,None,None,15,7]
root = TreeNode(root_values[0])
queue = [root]
i = 1

# Iterate over the list to assign children nodes
while i < len(root_values):
    current_node = queue.pop(0)
    
    # Assign the left child if it's not None
    if root_values[i] is not None:
        current_node.left = TreeNode(root_values[i])
        queue.append(current_node.left)
    i += 1

    # Check if there's a right child and we don't go out of bounds
    if i < len(root_values) and root_values[i] is not None:
        current_node.right = TreeNode(root_values[i])
        queue.append(current_node.right)
    i += 1
print(solution.maxDepth(root))
