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
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return -1
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """You are given an m x n 2-D integer array matrix and an integer target.
        Each row in matrix is sorted in non-decreasing order.
        The first integer of every row is greater than the last integer of the previous row.
        Return true if target exists within matrix or false otherwise.
        Can you write a solution that runs in O(log(m * n)) time?"""
        top, bottom = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        row = 0
        
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
            
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
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
                    

class TimeMap:
    """Implement a time-based key-value data structure that supports:
    Storing multiple values for the same key at specified time stamps.
    Retrieving the key's value at a specified timestamp."""
    
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """void set(String key, String value, int timestamp) 
        Stores the key key with the value value at the given time timestamp."""
        
        if key not in self.store:
            self.store[key] = []
        self.store[key].appened([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        """String get(String key, int timestamp) Returns the most recent value of key 
        if set was previously called on it and the most recent timestamp for that key 
        prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). 
        If there are no values, it returns "". """
        result = ""
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                result = values[mid][0]
                l = mid + 1      
            else:
                r = mid - 1
                
        return result

solution = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15
print(solution.searchMatrix(matrix, target))
