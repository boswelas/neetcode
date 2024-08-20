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

solution = Solution()
s = "]]"
print(solution.isValid(s))
