class Solution:
    def is_palindrome(self, s):
        """Given a string s, return true if it is a palindrome, otherwise return false.
        A palindrome is a string that reads the same forward and backward. It is also 
        case-insensitive and ignores all non-alphanumeric characters."""
        l, r = 0, len(s)-1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
    
solution = Solution()
s = ".,"
print(solution.is_palindrome(s))
