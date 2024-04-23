from collections import defaultdict
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


    def isAnagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
        all the original letters exactly once."""

        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return indices of the two numbers such that they add
        up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order."""

        for i in range(len(nums) - 1):
            needed = target - nums[i]
            if needed in nums[i + 1:]:
                return [i, nums[i + 1:].index(needed) + i + 1]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
        all the original letters exactly once."""
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())











solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = solution.groupAnagrams(strs)
print(result)

