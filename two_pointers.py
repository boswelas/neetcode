from typing import List


class Solution:
    
    def is_palindrome(self, s):
        """Given a string s, return true if it is a palindrome, otherwise return false.
        A palindrome is a string that reads the same forward and backward. It is also 
        case-insensitive and ignores all non-alphanumeric characters."""
        l, r = 0, len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Given an array of integers numbers that is sorted in non-decreasing order.
        Return the indices (1-indexed) of two numbers, [index1, index2], such that they add 
        up to a given target number target and index1 < index2. Note that index1 and index2 
        cannot be equal, therefore you may not use the same element twice.
        There will always be exactly one valid solution.
        Your solution must use O(1) additional space."""
        l, r = 0, len(numbers) - 1
        
        while l < r:
            temp = numbers[l] + numbers[r]
            if temp == target:
                return [l+1, r+1]
            elif temp > target:
                r -= 1
            else:
                l += 1
   
                
    
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
    
    def maxArea(self, height: List[int]) -> int:
        """You are given an integer array heights where heights[i] represents 
        the height of the ith bar.
        You may choose any two bars to form a container. Return the maximum 
        amount of water a container can store."""
        area = 0
        l, r = 0, len(height) - 1

        while l < r:
            temp = min(height[l], height[r])
            area = max(area, (temp * (r - l)))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return area
    
    def trap(self, height: List[int]) -> int:
        """You are given an array non-negative integers heights which represent an 
        elevation map. Each value heights[i] represents the height of a bar, which 
        has a width of 1.
        Return the maximum area of water that can be trapped between the bars."""
        
        if not height or len(height) == 1:
            return 0
        
        total = 0
        max_height = height.index(max(height))
        l_array = height[:max_height + 1]
        r_array = height[max_height:]

        #get left side
        while len(l_array) > 1:
            l_max = len(l_array) - 1
            l = l_array.index(max(l_array[:l_max]))
            space = l_array[l] * (l_max - l - 1)
            for i in range(l + 1, l_max):
                space -= l_array[i]
            total += space
            l_array = l_array[:l + 1]
            
        #get right side
        while len(r_array) > 1:
            r = r_array[1:].index(max(r_array[1:])) + 1
            space = r_array[r] * (r - 1)
            for i in range(1, r):
                space -= r_array[i]
            total += space
            r_array = r_array[r:]      
                
        return total
        
    
solution = Solution()
numbers = [1,2,3,4]
target = 3
print(solution.twoSum(numbers, target))
