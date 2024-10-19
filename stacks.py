from typing import List


class MinStack:
    """Design a stack class that supports the push, pop, top, and getMin operations.
    MinStack() initializes the stack object. Each function should run in O(1) time."""
    
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
        
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]

class Solution:
    
    def isValid(self, s: str) -> bool:
        """You are given a string s consisting of the following characters: 
        '(', ')', '{', '}', '[' and ']'. The input string s is valid if and only if:
        Every open bracket is closed by the same type of close bracket.
        Open brackets are closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type."""
        pairs = {")":"(", "}":"{", "]":"["}
        stack = []
        
        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

    def evalRPN(self, tokens: List[str]) -> int:
        """You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
        Return the integer that represents the evaluation of the expression.
        The operands may be integers or the results of other operations.
        The operators include '+', '-', '*', and '/'.
        Assume that division between integers always truncates toward zero."""
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b/a)))
            else:
                stack.append(int(t))
        return stack[0]
        
    def generateParenthesis(self, n: int) -> List[str]:
        """You are given an integer n. Return all well-formed parentheses strings 
        that you can generate with n pairs of parentheses. 1 <= n <= 7"""      
        result = []
        stack = []
        
        def backtrack(openP, closedP):
            if openP == closedP == n:
                result.append("".join(stack))
                return
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closedP)
                stack.pop()
            if closedP < openP:
                stack.append(")")
                backtrack(openP, closedP + 1)
                stack.pop()
                
        backtrack(0, 0)
        return result
        
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """You are given an array of integers temperatures where temperatures[i] 
        represents the daily temperatures on the ith day.
        Return an array result where result[i] is the number of days after the ith day 
        before a warmer temperature appears on a future day. If there is no day in the 
        future where a warmer temperature will appear for the ith day, set result[i] to 0 instead."""
        stack = []
        result = [0] * len(temperatures)
        
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, i = stack.pop()
                result[i] = index - i
            stack.append([temp, index])
        return result

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
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        
        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
                
        return len(stack)
        
        
       
solution = Solution()
n = 3
print(solution.generateParenthesis(n))
