# 'NeetCode Roadmap'
# 'Dec 11, 2023'

from typing import List
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
                answer.append("". join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
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





solution = Solution()
piles = [3,6,7,11]
h = 8
result = solution.minEatingSpeed(piles, h)
print(result)
print("expected: 4")
