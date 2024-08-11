from typing import List


class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        """You are given an array of distinct integers nums, sorted in ascending order, 
        and an integer target.
        Implement a function to search for target within nums. If it exists, then return its index, 
        otherwise, return -1."""
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + ((r-l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                        
        return -1
        
        
solution = Solution()
nums = [-1,0,2,4,6,8]
target = 4
print(solution.search(nums, target))
