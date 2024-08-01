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

    
solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(solution.topKFrequent(nums, k))
