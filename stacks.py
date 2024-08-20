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

    
    



solution = Solution()
s = "]]"
print(solution.isValid(s))
