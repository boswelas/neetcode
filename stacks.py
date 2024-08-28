from typing import List


class MinStack:
    """Design a stack class that supports the push, pop, top, and getMin operations.
    MinStack() initializes the stack object. Each function should run in O(1) time."""
    
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """void push(int val) pushes the element val onto the stack."""
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        """void pop() removes the element on the top of the stack."""
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """int top() gets the top element of the stack."""
        return self.stack[-1]

    def getMin(self) -> int:
        """int getMin() retrieves the minimum element in the stack."""
        return self.min_stack[-1]

class Solution:
    
    def isValid(self, s: str) -> bool:
        """You are given a string s consisting of the following characters: 
        '(', ')', '{', '}', '[' and ']'. The input string s is valid if and only if:
        Every open bracket is closed by the same type of close bracket.
        Open brackets are closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type."""
        stack = []
        
        for val in s:
            if val == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(val)
            elif val == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(val)
            elif stack and val == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(val)
            else:
                stack.append(val)
        
        if len(stack) == 0:
            return True
        return False


    def evalRPN(self, tokens: List[str]) -> int:
        """You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
        Return the integer that represents the evaluation of the expression.
        The operands may be integers or the results of other operations.
        The operators include '+', '-', '*', and '/'.
        Assume that division between integers always truncates toward zero."""
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
    
    def generateParenthesis(self, n: int) -> List[str]:
        """You are given an integer n. Return all well-formed parentheses strings 
        that you can generate with n pairs of parentheses. 1 <= n <= 7"""
        stack = []
        result = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
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
        return result
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """You are given an array of integers temperatures where temperatures[i] 
        represents the daily temperatures on the ith day.
        Return an array result where result[i] is the number of days after the ith day 
        before a warmer temperature appears on a future day. If there is no day in the 
        future where a warmer temperature will appear for the ith day, set result[i] to 0 instead."""
        days = []
        
        for i in range(0, len(temperatures)):
            count = 0
            for k in range(i+1, len(temperatures)):
                count += 1
                if temperatures[k] > temperatures[i]:
                    days.append(count)
                    break
            if len(days) < i + 1:
                days.append(0)
            
        return days
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """There are n cars traveling to the same destination on a one-lane highway.
        You are given two arrays of integers position and speed, both of length n.
            position[i] is the position of the ith car (in miles)
            speed[i] is the speed of the ith car (in miles per hour)
            The destination is at position target miles.
        A car cannot pass another car ahead of it. It can only catch up to another car and then drive at the 
        same speed as the car ahead of it.
        A car fleet is a non-empty set of cars driving at the same position and same speed. 
        A single car is also considered a car fleet.
        If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered 
        to be part of the fleet.
        Return the number of different car fleets that will arrive at the destination."""
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        stack = []
        
        for p, s in pair: 
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

                
    
    



solution = Solution()
target = 13
position = [10,2,5,7,4,6,11]
speed = [7,5,10,5,9,4,1]
print(solution.carFleet(target, position, speed))
