from typing import List
from collections import deque


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
                    
        
    
solution = Solution()
grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
print(solution.numIslands(grid))
