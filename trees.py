from cmath import inf
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """You are given the root of a binary tree root. Invert the binary tree and return its root."""
        if root is None:
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
            
            l_height = dfs(root.left)
            r_height = dfs(root.right)
            
            curr = l_height + r_height
            result[0] = max(result[0], curr)
            
            return 1 + max(l_height, r_height)
        dfs(root)
        return result[0]
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Given a binary tree, return true if it is height-balanced and false otherwise.
        A height-balanced binary tree is defined as a binary tree in which the left and right subtrees 
        of every node differ in height by no more than 1."""
        result = [0]
        
        def dfs(root):
            if root is None:
                return 0
            
            l_height = dfs(root.left)
            r_height = dfs(root.right)
            
            result[0] = max(result[0], abs(l_height - r_height))
            
            return 1 + max(l_height, r_height)            
            
        dfs(root)
        return result[0] < 2
                     
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
        Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values."""
        
        def isSame(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            else:
                return False
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
        
        def findSubTree(root):
            if not root:
                return False
            
            if isSame(root, subRoot):
                return True
            
            return findSubTree(root.left) or findSubTree(root.right)
            
        return findSubTree(root)
            
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        result = [root]
        
        def dfs(root):
            if root is None:
                return
            
            result.append(root)
            
            if root.val < p.val and root.val < q.val:
                dfs(root.right)
            elif root.val > p.val and root.val > q.val:
                dfs(root.left)
            else:
                return
        dfs(root)
        return result[-1]
                
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Given a binary tree root, return the level order traversal of it as a nested list, 
        where each sublist contains the values of nodes at a particular level in the tree, from left to right."""
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            
            count = len(queue)
            temp = []
            for i in range(count):
                if queue:
                    val = queue.popleft()
                    
                    if val:
                        temp.append(val.val)
                        queue.append(val.left)
                        queue.append(val.right)
            result.append(temp)
        return result[:-1]
                    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side 
        of the tree, ordered from top to bottom."""
        if root is None:
            return []
        
        result = []
        queue = deque()
        queue.append(root)
        
        while queue:
            count = len(queue)
            temp = []
            for i in range(count):
                val = queue.popleft()
                if val:
                    temp.append(val.val)
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
            result.append(temp[-1])
        return result
        
    def goodNodes(self, root: TreeNode) -> int:
        """Within a binary tree, a node x is considered good if the path from the root of the tree to the node x 
        contains no nodes with a value greater than the value of node x.
        Given the root of a binary tree root, return the number of good nodes within the tree."""
        if root is None:
            return 0
        
        result = 0
        stack = [[root, root.val]]
        
        while stack:
            node, currmax = stack.pop()
            
            if node:
                if node.val >= currmax:
                    result += 1
                if node.val > currmax:
                    currmax = node.val
                    
                if node.left:
                    stack.append([node.left, currmax])
                if node.right:
                    stack.append([node.right, currmax])            
        return result
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false."""
        def isValid(root, minVal, maxVal):
            if root is None:
                return True
            if minVal < root.val < maxVal:
                return isValid(root.left, minVal, root.val) and isValid(root.right, root.val, maxVal)
            else:
                return False
        return isValid(root, -inf, inf)
       
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
                
        


solution = Solution()    

root_values = [5,3,6,2,4,None,None,1] 
k = 6
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
    
print(solution.kthSmallest(root, k))
