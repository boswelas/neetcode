# 'NeetCode Roadmap'
# 'Dec 11, 2023'

from collections import Counter


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """Given an integer array nums, return true if any value appears at least twice in the array, and return false
        if every element is distinct."""
        dup_list = set()

        for val in nums:
            if val in dup_list:
                return True
            else:
                dup_list.add(val)

        return False

    def isAnagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
        all the original letters exactly once."""

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Given an array of integers nums and an integer target, return indices of the two numbers such that they add
        up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order."""

        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return []

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
        using all the original letters exactly once."""

        sorted_dict = {}
        sorted_array = []

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in sorted_dict:
                sorted_dict[sorted_word] = len(sorted_array)
                sorted_array.append([word])
            else:
                sorted_array[sorted_dict[sorted_word]].append(word)

        return sorted_array

    # 'Dec 13, 2023'
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order."""

        counter = Counter(nums)
        return [key for key, _ in counter.most_common(k)]

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
        elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation."""

        length = len(nums)
        prefix = []
        suffix = []
        answer = []

        prefix_sol = 1
        suffix_sol = 1

        for i in range(0, length):
            prefix.append(prefix_sol)
            prefix_sol *= nums[i]

        for i in range(length-1, -1, -1):
            suffix.append(suffix_sol)
            suffix_sol *= nums[i]

        for i in range(0, length):
            answer.append(prefix[i] * suffix[length - i - 1])

        return answer


solution = Solution()
nums = [1,2,3,4]
result = solution.productExceptSelf(nums)
print(result)
