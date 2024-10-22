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
            return 
        
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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        
        def height(root):
            if not root:
                return 0
            
            left_height = height(root.left)
            if balanced[0] is False:
                return 0
            
            right_height = height(root.right)
            
            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left_height, right_height)
        
        height(root)
        return balanced[0]

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(p, q)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            
            if p.val != q.val:
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def has_subtree(root):
            if not root:
                return False
            
            if sameTree(root, subRoot):
                return True
            
            return has_subtree(root.left) or has_subtree(root.right)
        
        return has_subtree(root)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]
        
        def search(root):
            if not root: 
                return
            
            lca[0] = root
            
            if root is p or root is q:
                return
            
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                return
            
        search(root)
        return lca[0]
            
            

solution = Solution()    
root_values = [1,2,3,None,None,4]
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
print(solution.isBalanced(root))
