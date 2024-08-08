from typing import List


class Solution:
    def is_palindrome(self, s):
        """Given a string s, return true if it is a palindrome, otherwise return false.
        A palindrome is a string that reads the same forward and backward. It is also 
        case-insensitive and ignores all non-alphanumeric characters."""
        l, r = 0, len(s)-1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Given an array of integers numbers that is sorted in non-decreasing order.
        Return the indices (1-indexed) of two numbers, [index1, index2], such that they add 
        up to a given target number target and index1 < index2. Note that index1 and index2 
        cannot be equal, therefore you may not use the same element twice.
        There will always be exactly one valid solution.
        Your solution must use O(1) additional space."""
        l, r = 0, 1
        
        while l < r:
            while r < len(numbers):
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
                r += 1
            l += 1
            r = l + 1
        return
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Given an integer array nums, return all the triplets 
        [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
        and the indices i, j and k are all distinct.
        The output should not contain any duplicate triplets. 
        You may return the output and the triplets in any order."""
        
        result = set()
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        
        return [list(s) for s in result]

    
solution = Solution()
nums = [0,0,0]
print(solution.threeSum(nums))
