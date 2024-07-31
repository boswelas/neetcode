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

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
        following rules:
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition."""
        # create DS for r and c, square
        # traverse board and add to r and c in dict
        # check if in key, if not add, else return false
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in squares[i//3, j//3]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    squares[i//3, j//3].add(board[i][j])

        return True

    def longestConsecutive(self, nums: List[int]) -> int:
        """Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        You must write an algorithm that runs in O(n) time."""
        output = 0

        return output

    def isPalindrome(self, s: str) -> bool:
        """A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
        all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
        and numbers.
        Given a string s, return true if it is a palindrome, or false otherwise."""
        forward = ""
        for char in s:
            if char.isdigit() or char.isalpha():
                forward = forward + char.lower()

        if forward == forward[::-1]:
            return True
        return False

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
        such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
        where 1 <= index1 < index2 <= numbers.length.
        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2]
        of length 2.
        The tests are generated such that there is exactly one solution. You may not use the same element twice.
        Your solution must use only constant extra space."""
        #l, r pointers
        l = 0
        r = len(numbers) - 1
        mid = len(numbers) // 2

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
        and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets."""
        output = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return output

    def maxArea(self, height: List[int]) -> int:
        """You are given an integer array height of length n. There are n vertical lines drawn such that the two
        endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.
        Notice that you may not slant the container."""
        output = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            output = max(area, output)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return output

    def trap(self, height: List[int]) -> int:
        """Given n non-negative integers representing an elevation map where the width of each bar is 1, compute
        how much water it can trap after raining."""
        #find max
        # find second max
        # mul distance by sm
        # sub numbers between
        # add that to output
        # set sm to max and find new max
        output = 0
        max_height = height.index(max(height))

        r_array = height[max_height:]
        l = 0

        while l < len(height):
            second_max = r_array.index(max(r_array[1:]))
            area = r_array[second_max] * (r_array[l] - 1)
            output += area
            l = second_max
        return output

solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = solution.trap(height)
print(result)

