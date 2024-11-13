from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
        An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
        You may assume water is surrounding the grid (i.e., all the edges are water)."""   
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
                return
            else:
                grid[i][j] = "0"
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i - 1, j)
                
        
        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    result += 1
                    dfs(i, j)
                    
        return result
                    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
        An island is defined as a group of 1's connected horizontally or vertically. 
        You may assume all four edges of the grid are surrounded by water.
        The area of an island is defined as the number of cells within the island.
        Return the maximum area of an island in grid. If no island exists, return 0."""
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        result = 0
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return 0
            else:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))
                    
        return result
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """Given a node in a connected undirected graph, return a deep copy of the graph.
        Each node in the graph contains an integer value and a list of its neighbors."""
        if not node:
            return None
        
        start = node 
        node_ref = {}
        stack = [node]
        visited = set()
        visited.add(start)
        
        while stack:
            node = stack.pop()
            node_ref[node] = Node(node.val)
            for n in node.neighbors:
                if n not in visited:
                    visited.add(n)
                    stack.append(n)
        
        for old_node, new_node in node_ref.items():
            for n in old_node.neighbors:
                new_n = node_ref[n]
                new_node.neighbors.append(new_n)
                
        return node_ref[start]
                        
        
        


solution = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(solution.maxAreaOfIsland(grid))
