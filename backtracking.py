from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Given an array nums of unique integers, return all possible subsets of nums.
        The solution set must not contain duplicate subsets. You may return the solution in any order."""
        res = []
        sol = []
        
        def backtrack(i):
            if i == len(nums):
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
        """You are given an array of distinct integers nums and a target integer target. 
        Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target."""
        res = []
        
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
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
        """Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order."""
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
        nums.sort()
        
        def backtrack(i):
            if i == len(nums):
                res.add(tuple(sol))
                return
            
            backtrack(i + 1)
            
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
            
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
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target:
                    break
                
                curr.append(candidates[j])
                backtrack(j + 1, curr, total + candidates[j])
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
        res, sol = [], []
        
        def backtrack(i):
            if i >= len(s):
                res.append(sol.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    sol.append(s[i:j+1])
                    backtrack(j + 1)
                    sol.pop()
                    
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        backtrack(0)
        return res
                    
    def letterCombinations(self, digits: str) -> List[str]:
        """You are given a string digits made up of digits from 2 through 9 inclusive.
        Each digit (not including 1) is mapped to a set of characters as shown below:
        A digit could represent any one of the characters it maps to.
        Return all possible letter combinations that digits could represent. You may return the answer in any order."""

            
            
              
            
        
        
    
solution = Solution()
s = "aab"
print(solution.partition(s))
