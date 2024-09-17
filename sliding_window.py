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
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """You are given two strings s1 and s2.
        Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation 
        of s1 exists as a substring of s2, then return true.
        Both strings only contain lowercase letters."""
        if len(s1) > len(s2):
            return False
        
        s1_dict = {}
        s2_dict = {}
        l, r = 0, len(s1) - 1
       
        for char in s1:
            if char not in s1_dict:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1
                
        for i in range(0, len(s1)):
            if s2[i] not in s2_dict:
                s2_dict[s2[i]] = 1
            else:
                s2_dict[s2[i]] += 1
            if s1_dict == s2_dict:
                return True
            
        while r < len(s2) - 1:
            s2_dict[s2[l]] -= 1
            if s2_dict[s2[l]] == 0:
                del s2_dict[s2[l]]
            l += 1
            r += 1
            
            if s2[r] not in s2_dict:
                    s2_dict[s2[r]] = 1
            else:
                s2_dict[s2[r]] += 1      
            if s1_dict == s2_dict:
                return True      
            
        return False
    
    
    def minWindow(self, s: str, t: str) -> str:
        """Given two strings s and t, return the shortest substring of s such that 
        every character in t, including duplicates, is present in the substring. 
        If such a substring does not exist, return an empty string "".
        You may assume that the correct output is always unique."""
        if len(t) > len(s):
            return ""
        
        t_sorted = "".join(sorted(t))
        result = s
        curr = ""
        l, r = 0, 0
        
        while r < len(s):
            curr += s[r]
            if t_sorted in "".join(sorted(curr)):
                if len(curr) < len(result):
                    result = curr
                l += 1
                curr = curr[1:]
            else:
                r += 1
        
        return result   
        
    
    
solution = Solution()
s = "OUZODYXAZV"
t = "XYZ"
print(solution.minWindow(s, t))
