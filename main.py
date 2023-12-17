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

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
        following rules:
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        """
        board_dict = {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": []}

        for i in range(len(board)):
            for j in range(len(board[i])):
                value = board[i][j]
                if value != ".":
                    if i in (0, 1, 2):
                        if j in (0, 1, 2):
                            grid = 1
                        elif j in (3, 4, 5):
                            grid = 2
                        else:
                            grid = 3
                    elif i in (3, 4, 5):
                        if j in (0, 1, 2):
                            grid = 4
                        elif j in (3, 4, 5):
                            grid = 5
                        else:
                            grid = 6
                    else:
                        if j in (0, 1, 2):
                            grid = 7
                        elif j in (3, 4, 5):
                            grid = 8
                        else:
                            grid = 9
                    if any(entry[0] == i or entry[1] == j or entry[2] == grid for entry in board_dict.get(value, [])):
                        return False
                    board_dict.setdefault(value, []).append((i, j, grid))

        return True

    def longestConsecutive(self, nums: list[int]) -> int:
        """Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        You must write an algorithm that runs in O(n) time."""
        if len(nums) < 1:
            return 0

        answer = 1
        count = 1
        sorted_nums = sorted(nums)

        for i in range(0, len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1] - 1:
                count += 1
                if count > answer:
                    answer = count
            elif sorted_nums[i] == sorted_nums[i + 1]:
                continue
            else:
                count = 1

        return answer

solution = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
result = solution.longestConsecutive(nums)
print(result)
