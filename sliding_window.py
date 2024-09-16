from typing import List


class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        """You are given an integer array prices where prices[i] is the price of
        NeetCoin on the ith day.
        You may choose a single day to buy one NeetCoin and choose a different day
        in the future to sell it.
        Return the maximum profit you can achieve. You may choose to not make any transactions, 
        in which case the profit would be 0."""
        profit = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            profit = max(profit, price - lowest)
        return profit
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string s, find the length of the longest substring without 
        duplicate characters.
        A substring is a contiguous sequence of characters within a string."""
        queue = []
        result = 0
        
        for char in s:
            if char not in queue:
                queue.append(char)
            else:
                while queue[0] != char:
                    queue.pop(0)
                queue.pop(0)
                queue.append(char)   
            result = max(result, len(queue))             
        
        return result
    
    
    def characterReplacement(self, s: str, k: int) -> int:
        """You are given a string s consisting of only uppercase english characters 
        and an integer k. You can choose up to k characters of the string and replace 
        them with any other uppercase English character.
        After performing at most k replacements, return the length of the longest substring 
        which contains only one distinct character."""
        result = 0
        characters = {}
        l, r = 0, 0
        total = 0
        
        while r < len(s):
            if s[r] not in characters:
                characters[s[r]] = 1
            else:
                characters[s[r]] += 1
            total += 1
            diff = total - max(characters.values())
            if diff <= k:
                result = max(result, total)
                r += 1
            else:
                characters[s[l]] -= 1
                total -= 1
                l += 1
                r += 1
                
        return result
            
        
        
        
       

    
    
solution = Solution()
s = "AAABABB" 
k = 1
print(solution.characterReplacement(s, k))
