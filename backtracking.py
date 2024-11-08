from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtrack(i):
            if i == n:
                res.append(sol.copy())
                return
            
            #don't include
            backtrack(i + 1)
            
            #include
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        backtrack(0)
        return res
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
       
        def backtrack(i, curr, total):
            if total == target:
               res.append(curr.copy())
               return
               
            if i >= len(candidates) or total > target:
                return
            
            #don't include
            backtrack(i + 1, curr, total)
            
            #include
            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            curr.pop()
            
        backtrack(0, [], 0)
        return res
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        
        def backtrack():
            if len(sol) == n:
                res.append(sol.copy())
                
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        backtrack()
        return res
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """You are given an array nums of integers, which may contain duplicates. Return all possible subsets.
        The solution must not contain duplicate subsets. You may return the solution in any order."""
        res = set()
        sol = []
        n = len(nums)
        
        def backtrack(i):
            if i == n:
                res.add(tuple(sol))
                return
            
            # don't include
            backtrack(i + 1)
            
            #include
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
            
        nums.sort()
        backtrack(0)
        return [list(val) for val in res]
                
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """You are given an array of integers candidates, which may contain duplicates, and a target integer target. 
        Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.
        Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.
        You may return the combinations in any order and the order of the numbers in each combination can be in any order."""
        res = []
        candidates.sort()
        
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()
            
        backtrack(0, [], 0) 
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        """Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.
        For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. 
        The same cell may not be used more than once in a word."""
        ROWS, COLS = len(board), len(board[0])
        curr = set()
        
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in curr:
                return False
            
            curr.add((r, c))
            res = (backtrack(r + 1, c, i + 1) or
            backtrack(r - 1, c, i + 1) or
            backtrack(r, c + 1, i + 1) or
            backtrack(r, c - 1, i + 1))
            
            curr.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0): return True
        return False
            
    def partition(self, s: str) -> List[List[str]]:
        """Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.
        You may return the solution in any order."""
    
solution = Solution()
s = "aab"
print(solution.partition(s))
