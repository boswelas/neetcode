import math
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
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """You are given an m x n 2-D integer array matrix and an integer target.
        Each row in matrix is sorted in non-decreasing order.
        The first integer of every row is greater than the last integer of the previous row.
        Return true if target exists within matrix or false otherwise.
        Can you write a solution that runs in O(log(m * n)) time?"""
        for i in range(len(matrix)-1, -1, -1):
            if matrix[i][0] <= target:
                break  
        
        l, r = 0, len(matrix[i]) - 1
        
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """You are given an integer array piles where piles[i] is the number of bananas 
        in the ith pile. You are also given an integer h, which represents the number of 
        hours you have to eat all the bananas.
        You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a 
        pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
        you may finish eating the pile but you can not eat from another pile in the same hour.
        Return the minimum integer k such that you can eat all the bananas within h hours."""
        
        l = 1
        r = max(piles)
        result = r
        
        while l <= r:
            banana_time = 0
            mid = (l + r) // 2
            for banana in piles:
                banana_time += banana // mid
                if banana % mid  != 0:
                    banana_time += 1
            if banana_time <= h:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result

    def findMin(self, nums: List[int]) -> int:
        """You are given an array of length n which was originally sorted in ascending order. 
        It has now been rotated between 1 and n times. Assuming all elements in the rotated 
        sorted array nums are unique, return the minimum element of this array.
        A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?"""
        min_num = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] < min_num:
                min_num = nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
                
        return min_num
    
    
    def search_rotated(self, nums: List[int], target: int) -> int:
        """You are given an array of length n which was originally sorted in ascending order. 
        It has now been rotated between 1 and n times. Given the rotated sorted array nums and 
        an integer target, return the index of target within nums, or -1 if it is not present."""

        l, r = 0, len(nums) -1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1
                    
        
solution = Solution()
nums = [3,4,5,6,1,2] 
target = 6
print(solution.search_rotated(nums, target))
