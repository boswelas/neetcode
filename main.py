# 'NeetCode Roadmap'
# 'Dec 11, 2023'
import collections
from typing import List
from collections import Counter
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


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

        for i in range(length - 1, -1, -1):
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

    def encode(self, strs):
        """Design an algorithm to encode a list of strings to a string.
        The encoded string is then sent over the network and is decoded back to the original list of strings."""
        answer = ""
        for val in range(0, len(strs)):
            answer += strs[val] + " "
        return solution.decode(answer)

    def decode(self, strs):
        answer = []
        temp = ""

        for char in strs:
            if char != " ":
                temp += char
            if char == " ":
                answer.append(temp)
                temp = ""

        return answer

    def isPalindrome(self, s: str) -> bool:
        """A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
        non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
        and numbers. Given a string s, return true if it is a palindrome, or false otherwise."""

        palin_string = ""

        for char in s:
            if char.isalnum():
                palin_string += char.lower()

        length = len(palin_string)
        if length / 2 != 0:
            length -= 1

        count = 0
        front = 0
        back = length

        while count < length:
            if palin_string[front] != palin_string[back]:
                return False
            else:
                count += 2
                front += 1
                back -= 1

        return True

    def twoSum_2(self, numbers: list[int], target: int) -> list[int]:
        """Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
        such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
        where 1 <= index1 < index2 <= numbers.length.
        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of
        length 2.
        The tests are generated such that there is exactly one solution. You may not use the same element twice.
        Your solution must use only constant extra space."""
        index1 = 0
        index2 = 1

        while index1 <= len(numbers) - 1:
            if numbers[index1] + numbers[index2] == target:
                return [index1 + 1, index2 + 1]
            elif numbers[index1] == numbers[index2]:
                index1 += 1
                index2 = index1 + 1
            elif numbers[index1] + numbers[index2] > target:
                index1 += 1
                index2 = index1 + 1
            elif index2 == len(numbers) - 1:
                index1 += 1
                index2 = index1 + 1
            else:
                index2 += 1

        return []

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
        and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets."""
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

    def maxArea(self, height: list[int]) -> int:
        """You are given an integer array height of length n. There are n vertical lines drawn such that the two
        endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store."""
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0

        while left_pointer < right_pointer:
            h = min(height[left_pointer], height[right_pointer])
            w = right_pointer - left_pointer
            max_area = max(max_area, h * w)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area

    def trap(self, height: list[int]) -> int:
        """Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it can trap after raining."""

        if len(height) < 3:
            return 0

        answer = 0
        max_value = max(height)
        max_index = height.index(max_value)

        left_array = height[:max_index + 1]
        print("left original is ", left_array)
        right_array = height[max_index:]
        print("right original is ", right_array)

        if len(left_array) > 2:
            left_max = len(left_array) - 1
            left_new_max = 0
            while left_max > 1:
                for i in range(0, left_max):
                    if left_array[i] > left_array[left_new_max]:
                        left_new_max = i
                left_val = left_array[left_new_max] * (left_max - left_new_max - 1)
                l_minus_amount = 0
                for i in range(left_new_max + 1, left_max):
                    l_minus_amount += left_array[i]
                left_val -= l_minus_amount
                print("left val is ", left_val)
                if left_val > 0:
                    answer += left_val
                left_max = left_new_max
                left_new_max = 0
                print("left max is ", left_max)

        if len(right_array) > 2:
            right_max = 0
            right_new_max = 1
            while right_max < len(right_array) - 2:
                for i in range(len(right_array) - 1, right_max, -1):
                    if right_array[i] >= right_array[right_new_max]:
                        right_new_max = i
                right_val = right_array[right_new_max] * (right_new_max - right_max - 1)
                r_minus_amount = 0
                for i in range(right_max + 1, right_new_max):
                    r_minus_amount += right_array[i]
                right_val -= r_minus_amount
                print("right val is ", right_val)
                if right_val > 0:
                    answer += right_val
                right_max = right_new_max
                right_new_max = right_max + 1
                print("right max is ", right_max)

        return answer

    def isValid(self, s: str) -> bool:
        """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
        string is valid.
        An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type."""
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            elif char == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(char)
            elif char == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)
            elif char == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(char)

        if len(stack) == 0:
            return True

        return False

    class MinStack:
        """Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
        Implement the MinStack class:
        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.
        You must implement a solution with O(1) time complexity for each function."""

        def __init__(self):
            self.stack = []
            self.min = []

        def push(self, val: int) -> None:
            self.stack.append(val)
            if not self.min or self.min[-1] > val:
                self.min.append(val)
            else:
                still_min = self.min[-1]
                self.min.append(still_min)

        def pop(self) -> None:
            self.stack.pop()
            self.min.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min[-1]

    def evalRPN(self, tokens: list[str]) -> int:
        """You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish
        Notation.
        Evaluate the expression. Return an integer that represents the value of the expression.
        Note that:
        The valid operators are '+', '-', '*', and '/'.
        Each operand may be an integer or another expression.
        The division between two integers always truncates toward zero.
        There will not be any division by zero.
        The input represents a valid arithmetic expression in a reverse polish notation.
        The answer and all the intermediate calculations can be represented in a 32-bit integer.
        """
        nums = []

        for char in tokens:
            if char.isdigit():
                nums.append(int(char))
            elif char == "+":
                val1 = nums.pop()
                val2 = nums.pop()
                nums.append(val2 + val1)
            elif char == "-":
                val1 = nums.pop()
                val2 = nums.pop()
                nums.append(val2 - val1)
            elif char == "*":
                val1 = nums.pop()
                val2 = nums.pop()
                nums.append(val2 * val1)
            elif char == "/":
                val1 = nums.pop()
                val2 = nums.pop()
                nums.append(val2 // val1)

        return nums[0]

    def generateParenthesis(self, n: int) -> list[str]:
        """Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""
        answer = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                answer.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return answer

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Given an array of integers temperatures represents the daily temperatures, return an array answer such that
        answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no
        future day for which this is possible, keep answer[i] == 0 instead."""
        output = [0] * len(temperatures)
        stack = [[temperatures[0], 0]]

        for i in range(1, len(temperatures)):
            if temperatures[i] > stack[-1][0]:
                while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                    output[stack[-1][1]] = (i - stack[-1][1])
                    stack.pop()
                stack.append([temperatures[i], i])
            else:
                stack.append([temperatures[i], i])

        return output

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """There are n cars going to the same destination along a one-lane road. The destination is target miles away.
        You are given two integer array position and speed, both of length n, where position[i] is the position of the
        ith car and speed[i] is the speed of the ith car (in miles per hour).
        A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same
        speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is
        ignored (i.e., they are assumed to have the same position).
        A car fleet is some non-empty set of cars driving at the same position and same speed.
        Note that a single car is also a car fleet.
        If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
        Return the number of car fleets that will arrive at the destination."""
        stack = []

        combined = list(zip(position, speed))
        sorted_array = sorted(combined, key=lambda x: x[0])
        cars = [[pos, spd, (target - pos) / spd] for pos, spd in sorted_array]

        stack.append(cars[-1])

        for i in range(len(cars) - 2, -1, -1):
            if cars[i][2] > stack[-1][2]:
                stack.append(cars[i])

        return len(stack)

    def largestRectangleArea(self, heights: list[int]) -> int:
        """Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
        return the area of the largest rectangle in the histogram."""
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

    def search(self, nums: list[int], target: int) -> int:
        """Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
        to search target in nums. If target exists, then return its index. Otherwise, return -1.
        You must write an algorithm with O(log n) runtime complexity."""
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return -1

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """You are given an m x n integer matrix matrix with the following two properties:
        Each row is sorted in non-decreasing order.
        The first integer of each row is greater than the last integer of the previous row.
        Given an integer target, return true if target is in matrix or false otherwise.
        You must write a solution in O(log(m * n)) time complexity."""
        rows = len(matrix)
        columns = len(matrix[0])
        top = 0
        bottom = rows - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top <= bottom):
            return False

        row = (top + bottom) // 2
        l = 0
        r = columns - 1

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have
        gone and will come back in h hours.
        Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k
        bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any
        more bananas during this hour.
        Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
        Return the minimum integer k such that she can eat all the bananas within h hours."""
        low = 1
        high = max(piles)

        if h == len(piles):
            return high

        while low <= high:
            mid = (high + low) // 2
            k = 0  # how many hours to eat

            for bananas in piles:
                k += (bananas + mid - 1) // mid
            if k <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low

    def findMin(self, nums: List[int]) -> int:
        """Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
        the array nums = [0,1,2,4,5,6,7] might become:
        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.
        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1],
        a[2], ..., a[n-2]].
        Given the sorted rotated array nums of unique elements, return the minimum element of this array.
        You must write an algorithm that runs in O(log n) time."""
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

    def search2(self, nums: List[int], target: int) -> int:
        """There is an integer array nums sorted in ascending order (with distinct values).
        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
        (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1],
        ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
        [4,5,6,7,0,1,2].
        Given the array nums after the possible rotation and an integer target, return the index of target if it is in
        nums, or -1 if it is not in nums.
        You must write an algorithm with O(log n) runtime complexity."""
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    class TimeMap:
        """Design a time-based key-value data structure that can store multiple values for the same key at different
        time stamps and retrieve the key's value at a certain timestamp."""

        def __init__(self):
            """Initializes the object of the data structure."""
            self.store = {}  # key : list of [value, timestamp]

        def set(self, key: str, value: str, timestamp: int) -> None:
            """Stores the key key with the value value at the given time timestamp."""
            if key not in self.store:
                self.store[key] = []
            self.store[key].append([value, timestamp])

        def get(self, key: str, timestamp: int) -> str:
            """Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are
            multiple such values, it returns the value associated with the largest timestamp_prev. If there are no
            values, it returns ""."""
            res = ""
            values = self.store.get(key, [])
            left = 0
            right = len(values) - 1

            while left <= right:
                middle = (left + right) // 2
                if values[middle][1] <= timestamp:
                    res = values[middle][0]
                    left = middle + 1
                else:
                    right = middle - 1

            return res

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted
        arrays.
        The overall run time complexity should be O(log (m+n))."""
        A = nums1
        B = nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        left = 0
        right = len(A) - 1

        while True:
            i = (left + right) // 2
            j = half - i - 2
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + (min(Aright, Bright))) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1

    def maxProfit(self, prices: List[int]) -> int:
        """You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
        future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1

        return maxProfit

    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string s, find the length of the longest substring without repeating characters."""
        char_set = set()
        left = 0
        max_substring = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_substring = max(max_substring, right - left + 1)

        return max_substring

    def characterReplacement(self, s: str, k: int) -> int:
        """You are given a string s and an integer k. You can choose any character of the string and change it to any
        other uppercase English character. You can perform this operation at most k times.
        Return the length of the longest substring containing the same letter you can get after performing the above
        operations."""
        max_length = 0
        left = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while(right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
        In other words, return true if one of s1's permutations is the substring of s2."""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s1_hashmap = {}
        s2_hashmap = {}
        left = 0
        right = len(s1) - 1

        if len(s1) > len(s2):
            return False

        for char in alphabet:
            s1_hashmap[char] = 0
        for char in range(len(s1)):
            s1_hashmap[s1[char]] = 1 + s1_hashmap.get(s1[char], 0)

        for char in alphabet:
            s2_hashmap[char] = 0
        for char in range(len(s1)):
            s2_hashmap[s2[char]] = 1 + s2_hashmap.get(s2[char], 0)
            if s1_hashmap == s2_hashmap:
                return True

        while right < len(s2) - 1:
            right += 1
            s2_hashmap[s2[right]] = 1 + s2_hashmap.get(s2[right], 0)
            s2_hashmap[s2[left]] -= 1
            left += 1
            if s1_hashmap == s2_hashmap:
                return True
        return False

    def minWindow(self, s: str, t: str) -> str:
        """Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
         every character in t (including duplicates) is included in the window. If there is no such substring, return
         the empty string "". The testcases will be generated such that the answer is unique."""
        if t == "":
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """You are given an array of integers nums, there is a sliding window of size k which is moving from the very
        left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window
        moves right by one position. Return the max sliding window."""
        max_values = []
        count = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            while count and nums[count[-1]] < nums[r]:
                count.pop()
            count.append(r)

            if l > count[0]:
                count.popleft()

            if (r+1) >= k:
                max_values.append(nums[count[0]])
                l += 1
            r += 1

        return max_values

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Given the head of a singly linked list, reverse the list, and return the reversed list."""
        prev = None
        curr = head

        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
        return prev

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first
        two lists.
        Return the head of the merged linked list."""

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
        Do not return anything, modify head in-place instead."""
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        return

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Given the head of a linked list, remove the nth node from the end of the list and return its head."""
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """A linked list of length n is given such that each node contains an additional random pointer, which could
        point to any node in the list, or null.
        Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new
        node has its value set to the value of its corresponding original node. Both the next and random pointer of the
        new nodes should point to new nodes in the copied list such that the pointers in the original list and copied
        list represent the same list state. None of the pointers in the new list should point to nodes in the original
        list.
        For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the
        corresponding two nodes x and y in the copied list, x.random --> y.
        Return the head of the copied linked list."""
        oldToCopy = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
        reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a
        linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself."""
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Given head, the head of a linked list, determine if the linked list has a cycle in it.
        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
        following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
        connected to. Note that pos is not passed as a parameter.
        Return true if there is a cycle in the linked list. Otherwise, return false."""

        visited = {}

        cur = head
        while cur:
            if cur in visited:
                return True
            else:
                visited[cur] = True
                cur = cur.next

        return False



solution = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = solution.addTwoNumbers(l1, l2)
print(result)
print("expected: true")
