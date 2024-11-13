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
        
        if not grid:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
                return 
            else:
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        res = 0        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
                    
        return res                     
                    
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
        
        visited = set()
        start = node
        stack = [start]
        node_ref = {}
        
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                node_ref[curr] = Node(curr.val)
                for n in curr.neighbors:
                    stack.append(n)
        
        for key, value in node_ref.items():
            for n in key.neighbors:
                value.neighbors.append(node_ref[n])
                
        return node_ref[start]
           
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """You are given a mxn 2D grid initialized with these three possible values:
        -1: A water cell that can not be traversed.
        0: A treasure chest.
        INF: A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
        Fill each land cell with the distance to its nearest treasure chest. 
        If a land cell cannot reach a treasure chest than the value should remain INF.
        Assume the grid can only be traversed up, down, left, or right."""
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        
        def bfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append([r, c])
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
                    
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            dist += 1
            

        
        


solution = Solution()
grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
print(solution.islandsAndTreasure(grid))
