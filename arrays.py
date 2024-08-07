from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Given an integer array nums, return true if any value appears more than 
         once in the array, otherwise return false."""
        visited = {}
        for i in nums:
            if i not in visited:
                visited[i] = True
            else:
                return True
        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if the two strings are anagrams of each other, 
        otherwise return false. An anagram is a string that contains the exact same characters as 
        another string, but the order of the characters can be different."""
        if len(s) != len(t):
            return False
        
        visited = {}
        
        for char in s:
            if char not in visited:
                visited[char] = 1
            else:
                visited[char] += 1

        for char in t:
            if char in visited:
                visited[char] -= 1
                if visited[char] == 0:
                    visited.pop(char)
            else:
                return False
            
        if visited:
            return False
            
        return True
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return the indices i and j 
        such that nums[i] + nums[j] == target and i != j."""
        i = 0
        while i <= len(nums) - 2:
            j = i + 1
            while j <= len(nums)-1:
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j += 1
            i += 1
        return []
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Given an array of strings strs, group all anagrams together into sublists. 
        You may return the output in any order."""
        sorted_dict = {}
        anagram_list = []
        
        for i in range(0, len(strs)):
            res = ''.join(sorted(strs[i]))
            if res not in sorted_dict:
                sorted_dict[res] = [i]
            else:
                sorted_dict[res].append(i)
                
        for key in sorted_dict:
            item = []
            for value in sorted_dict[key]:
                item.append(strs[value])
            anagram_list.append(item)
            
        return anagram_list
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Given an integer array nums and an integer k, return the k most frequent elements 
        within the array."""
        visited = {}
        kfrequent = []
        
        for num in nums:
            if num not in visited:
                visited[num] = 1
            else:
                visited[num] += 1
                
        for i in range(0, k):
            frequent = max(visited, key=visited.get)
            kfrequent.append(frequent)
            visited.pop(frequent)
            
        return kfrequent
    
    def encode(self, strs: List[str]) -> str:
        """Design an algorithm to encode a list of strings to a single string. The 
        encoded string is then decoded back to the original list of strings."""
        strs_string = ""
        for i in range(0, len(strs)):
            strs_string += str(len(strs[i])) + "#" + strs[i]
        return strs_string
          
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            count = ""
            while s[i].isdigit():
                count += s[i]
                i += 1
            count = int(count)
            i += 1
            temp = ""
            while count > 0:
                temp += "".join(s[i])
                count -= 1
                i += 1
            result.append(temp)
            
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
        
        
        
        

        
    
solution = Solution()
nums = [2,20,4,10,3,4,5]
print(solution.longestConsecutive(nums))
