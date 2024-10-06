from collections import defaultdict
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Given an integer array nums, return true if any value appears more than 
         once in the array, otherwise return false."""
        values = set()

        for num in nums:
            if num in values:
                return True
            else:
                values.add(num)
        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if the two strings are anagrams of each other, 
        otherwise return false. An anagram is a string that contains the exact same characters as 
        another string, but the order of the characters can be different."""
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return the indices i and j 
        such that nums[i] + nums[j] == target and i != j."""
        values = {}
        
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in values:
                return [values[diff], i]
            else:
                values[nums[i]] = i
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Given an array of strings strs, group all anagrams together into sublists. 
        You may return the output in any order."""
        sorted_strs = {}
        result = []

        for s in strs:
            temp = ''.join(sorted(s))
            if temp in sorted_strs:
                result[sorted_strs[temp]].append(s)
            else:
                sorted_strs[temp] = len(result)
                result.append([s])

        return result
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Given an integer array nums and an integer k, return the k most frequent elements 
        within the array."""
        occurences = defaultdict(int)
        frequencies = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            occurences[num] += 1
            
        for n, c in occurences.items():
            frequencies[c].append(n)
            
        result = []
        
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                result.append(num)
                if len(result) == k:
                    return result 
    
    def encode(self, strs: List[str]) -> str:
        """Design an algorithm to encode a list of strings to a single string. The 
        encoded string is then decoded back to the original list of strings."""
        strs_encoded = ''
        for s in strs:
            strs_encoded = strs_encoded + str(len(s)) + "#" + s
        
        return strs_encoded
          
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            count = ''
            while s[i] != "#":
                count = count + s[i]
                i += 1
            i += 1
            count = int(count)
            result.append(s[i:i+count])
            i+=count
        
        return result
        
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Given an integer array nums, return an array output where output[i] is 
        the product of all the elements of nums except nums[i].
        Follow-up: Could you solve it in O(n) time without using the division operation?"""
        forward = [nums[0]]
        backward = [nums[-1]]
        output = []
        
        for i in range(1, len(nums)):
            forward.append(nums[i] * forward[i-1])

        k = 0
        for i in range(len(nums) - 2, 0, -1):
            backward.append(nums[i] * backward[k])
            k += 1
        backward.append(1)
        backward.reverse()

        for i in range(0, len(nums)):
            if i - 1 < 0:
                output.append(backward[i + 1])
            elif i + 1 == len(nums):
                output.append(forward[i - 1])
            else:
                output.append(forward[i - 1] * backward[i+1])

        return output
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if 
        the following rules are followed:
        Each row must contain the digits 1-9 without duplicates.
        Each column must contain the digits 1-9 without duplicates.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
        without duplicates.
        Return true if the Sudoku board is valid, otherwise return false"""
        row, col, squares = {}, {}, {}
        for i in range(9):
            row[i] = set()
            col[i] = set()
            for j in range(9):
                squares[i//3, j//3] = set()

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    num = board[i][j]
                    if num in row[i] or num in col[j] or num in squares[i//3, j//3]:
                        return False
                    row[i].add(num)
                    col[j].add(num)
                    squares[i//3, j//3].add(num)
 
        return True
    
    def longestConsecutive(self, nums: List[int]) -> int:
        """Given an array of integers nums, return the length of the longest consecutive 
        sequence of elements.
        A consecutive sequence is a sequence of elements in which each element is exactly 
        1 greater than the previous element.
        You must write an algorithm that runs in O(n) time."""
        if len(nums) == 1:
            return 1
        
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
                
        return longest
    
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
        0 <= i, j, k, l < n
        nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0"""
        tuples = 0
        
        #check 0 <= i, j, k, l < n
        #check nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
        
        return tuples
        
        
        
        

        
    
solution = Solution()
strs = ["neet","code","love","you"]
print(solution.decode(solution.encode(strs)))
