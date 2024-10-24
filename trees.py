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
        """Given the root of a binary tree, return its depth. The depth of a binary tree is defined as 
        the number of nodes along the longest path from the root node down to the farthest leaf node."""
        result = 0
        stack = [[root, 1]]
        
        while stack:
            root, depth = stack.pop()
            
            if root:
                result = max(result, depth)
                stack.append([root.left, depth + 1])
                stack.append([root.right, depth + 1])
                
        return result
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. 
        The path does not necessarily have to pass through the root.
        The length of a path between two nodes in a binary tree is the number of edges between the nodes.
        Given the root of a binary tree root, return the diameter of the tree."""
        result = [0]
        
        def dfs(root):
            if root is None:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            result[0] = max(result[0], leftHeight + rightHeight)
            
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return result[0]    
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Given a binary tree, return true if it is height-balanced and false otherwise.
        A height-balanced binary tree is defined as a binary tree in which the left and right subtrees 
        of every node differ in height by no more than 1."""
        result = [True]
        
        def dfs(root):
            if root is None:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            
            if abs(leftHeight - rightHeight) > 1:
                result[0] = False
            
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return result[0]
                   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
        Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values."""
        
        def isSame(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        return isSame(p, q)
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure 
        and node values of subRoot and false otherwise.
        A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
        The tree tree could also be considered as a subtree of itself."""

        def isSame(root, subRoot):
            if not root and not subRoot:
                return True
            
            if (root and not subRoot) or (subRoot and not root):
                return False
            
            if root.val != subRoot.val:
                return False
            
            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
        
        def hasSub(root):
            if not root:
                return False
            
            if isSame(root, subRoot):
                return True
            
            return hasSub(root.left) or hasSub(root.right)
        
        return hasSub(root)
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        result = [root]
        
        def dfs(root):
            if not root:
                return
            
            result.append(root)
            if root is p or root is q:
                return
            elif root.val < p.val and root.val < q.val:
                dfs(root.right)
            elif root.val > p.val and root.val > q.val:
                dfs(root.left)
            else:
                return
            
        dfs(root)
        return result[-1]

solution = Solution()    
root_values = [5,3,8,1,4,7,9,None,2] 
p = 3 
q = 4
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
print(solution.lowestCommonAncestor(root, p, q))
