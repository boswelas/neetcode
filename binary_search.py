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

        
        
solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(solution.searchMatrix(matrix, target))
