class Solution:
        def climbStairs(self, n: int) -> int:
            """You are given an integer n representing the number of steps to reach the top of a staircase. 
            You can climb with either 1 or 2 steps at a time.
            Return the number of distinct ways to climb to the top of the staircase."""
            
            if n <= 3:
                return n
            n1, n2 = 2, 3

            for i in range(4, n + 1):
                temp = n1 + n2
                n1 = n2
                n2 = temp
            return n2
                        
                


solution = Solution()
n = 5
print(solution.climbStairs(n))
