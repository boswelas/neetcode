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
    
    
solution = Solution()
nums = [1,2,3]
print(solution.subsets(nums))
