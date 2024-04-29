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

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order."""

        nums_dict = {}
        result = []

        for val in nums:
            if val not in nums_dict:
                nums_dict[val] = 1
            else:
                new_val = nums_dict.get(val)
                new_val += 1
                nums_dict[val] = new_val

        sorted_nums_dict = sorted(nums_dict, key=nums_dict.get, reverse=True)

        for i in range(0, k):
            result.append(sorted_nums_dict[i])
        return result

    def encode(self, strs: List[str]) -> str:
        """Design an algorithm to encode a list of strings to a single string."""
        result = ""
        for item in strs:
            count = str(len(item)) + "#"
            result = result + count + item
        return result

    def decode(self, s: str) -> List[str]:
        """The encoded string is then decoded back to the original list of strings."""
        decoded = []
        count = 0
        length = ""
        i = 0

        while i < len(s):
            if s[i] != "#":
                length = length + s[i]
                i += 1
            else:
                i += 1
                count += int(length)
                word = s[i:i + count]
                decoded.append(word)
                i += count
                count = 0
                length = ""
        return decoded

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
        elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation."""
        prefix = [nums[0]]
        postfix = [nums[len(nums) - 1]]
        output = []
        k = 0

        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[i-1])

        for i in range(len(nums) - 2, 0, -1):
            postfix.append(nums[i] * postfix[k])
            k += 1
        postfix.append(postfix[len(postfix) -1])
        postfix.reverse()

        for i in range(0, len(nums)):
            if i - 1 < 0:
                output.append(postfix[i + 1])
            elif i + 1 == len(nums):
                output.append(prefix[i - 1])
            else:
                output.append(prefix[i - 1] * postfix[i+1])

        return output

solution = Solution()
nums = [0, 0]
result = solution.productExceptSelf(nums)
print(result)

