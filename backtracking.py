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

    
solution = Solution()
candidates = [10,1,2,7,6,1,5] 
target = 8
print(solution.combinationSum2(candidates, target))
