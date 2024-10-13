from collections import defaultdict
import math
from typing import List


class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        """You are given an array of distinct integers nums, sorted in ascending order, 
        and an integer target.
        Implement a function to search for target within nums. If it exists, then return its index, 
        otherwise, return -1."""
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
       
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """You are given an m x n 2-D integer array matrix and an integer target.
        Each row in matrix is sorted in non-decreasing order.
        The first integer of every row is greater than the last integer of the previous row.
        Return true if target exists within matrix or false otherwise.
        Can you write a solution that runs in O(log(m * n)) time?"""
        rows = len(matrix)
        cols = len(matrix[0])
        top, bottom = 0, rows - 1
        l, r = 0, cols - 1
        row = 0
        while top <= bottom:
            row = (bottom + top) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            if matrix[row][-1] < target:
                top += 1
            elif matrix[row][0] > target:
                bottom -= 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r -= 1
            else:
                l += 1
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """You are given an integer array piles where piles[i] is the number of bananas 
        in the ith pile. You are also given an integer h, which represents the number of 
        hours you have to eat all the bananas.
        You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a 
        pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
        you may finish eating the pile but you can not eat from another pile in the same hour.
        Return the minimum integer k such that you can eat all the bananas within h hours."""
        l, r = 1, max(piles)
        res = r
        
        if len(piles) == h:
            return res

        while l <= r:
            mid = (l + r) // 2
            totalTime = 0
            for banana in piles:
                totalTime += (banana + mid - 1) // mid
            if totalTime <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
    
    def findMin(self, nums: List[int]) -> int:
        """You are given an array of length n which was originally sorted in ascending order. 
        It has now been rotated between 1 and n times. Assuming all elements in the rotated 
        sorted array nums are unique, return the minimum element of this array.
        A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?"""
        l, r = 0, len(nums) - 1
        result = nums[0]
        
        while l <= r:
            mid = (l + r) // 2
            result = min(result, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return result
            
    def search_rotated(self, nums: List[int], target: int) -> int:
        """You are given an array of length n which was originally sorted in ascending order. 
        It has now been rotated between 1 and n times. Given the rotated sorted array nums and 
        an integer target, return the index of target within nums, or -1 if it is not present."""
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
                    

class TimeMap:
    """Implement a time-based key-value data structure that supports:
    Storing multiple values for the same key at specified time stamps.
    Retrieving the key's value at a specified timestamp."""
    
    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """void set(String key, String value, int timestamp) 
        Stores the key key with the value value at the given time timestamp."""
        self.dict[key].append([str, value])       
      
        
    def get(self, key: str, timestamp: int) -> str:
        """String get(String key, int timestamp) Returns the most recent value of key 
        if set was previously called on it and the most recent timestamp for that key 
        prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). 
        If there are no values, it returns "". """
        
   
        
        
solution = Solution()
nums=[4,5,6,7,0,1,2]
target=0
print(solution.search_rotated(nums, target))
