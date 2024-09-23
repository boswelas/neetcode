from typing import List


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
        
        def minCostClimbingStairs(self, cost: List[int]) -> int:
            """You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor 
            of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
            You may choose to start at the index 0 or the index 1 floor.
            Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost."""
            cost.append(0)
            
            for i in range(len(cost)-3, -1, -1):
                cost[i] += min(cost[i + 1], cost[i + 2])
                
            return min(cost[0], cost[1])
        
        def rob(self, nums: List[int]) -> int:
            """You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
            The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
            You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security 
            system will automatically alert the police if two adjacent houses were both broken into.
            Return the maximum amount of money you can rob without alerting the police."""
            rob1, rob2 = 0, 0
            
            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
                
            return rob2
                


solution = Solution()
nums = [2,7,9,3,1]
print(solution.rob(nums))
