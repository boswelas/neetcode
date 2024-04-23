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


solution = Solution()
s = "rat"
t = "car"
result = solution.isAnagram(s, t)
print(result)

