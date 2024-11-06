from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            backtrack(i + 1)
            
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
            
        backtrack(0)
        return res
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """You are given an array of distinct integers nums and a target integer target. 
        Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
        The same number may be chosen from nums an unlimited number of times. 
        Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
        You may return the combinations in any order and the order of the numbers in each combination can be in any order."""
        res = []
        
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr[:])
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
        """Given an array nums of unique integers, return all the possible permutations. 
        You may return the answer in any order."""
        res, sol = [], []
        n = len(nums)
        
        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        backtrack()
        return res
        
    
    
solution = Solution()
nums = [1,2,3]
print(solution.permute(nums))
