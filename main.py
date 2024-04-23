from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Given an integer array nums, return true if any value appears at least twice in the array, and return false
        if every element is distinct."""
        visited = {}

        for n in nums:
            if n not in visited:
                visited[n] = "n"
            else:
                return True
        return False

solution = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
result = solution.containsDuplicate(nums)
print(result)

