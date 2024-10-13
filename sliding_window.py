import string
from typing import List
from collections import Counter



class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        """You are given an integer array prices where prices[i] is the price of
        NeetCoin on the ith day.
        You may choose a single day to buy one NeetCoin and choose a different day
        in the future to sell it.
        Return the maximum profit you can achieve. You may choose to not make any transactions, 
        in which case the profit would be 0."""
        profit = 0
        l, r = 0, 1
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(prices[r] - prices[l], profit)
            else:
                l = r
            r += 1
        return profit
            
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string s, find the length of the longest substring without 
        duplicate characters.
        A substring is a contiguous sequence of characters within a string."""
        s_set = set()
        longest = 0
        l = 0
        
        for char in s:
            while char in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(char)
            longest = max(longest, len(s_set))
            
        return longest
       
    def characterReplacement(self, s: str, k: int) -> int:
        """You are given a string s consisting of only uppercase english characters 
        and an integer k. You can choose up to k characters of the string and replace 
        them with any other uppercase English character.
        After performing at most k replacements, return the length of the longest substring 
        which contains only one distinct character."""
        result = 0
        chars = {}
        l = 0
        max_val = 0
        
        for r in range(0, len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)    
            max_val = max(max_val, chars[s[r]])
            if (r - l + 1) - max_val > k:
                chars[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
            
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """You are given two strings s1 and s2.
        Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation 
        of s1 exists as a substring of s2, then return true.
        Both strings only contain lowercase letters."""
        if len(s1) > len(s2):
            return False
        
        s1_dict = dict.fromkeys(string.ascii_lowercase, 0)
        s2_dict = dict.fromkeys(string.ascii_lowercase, 0)
        
        for i in range(len(s1)):
            s1_dict[s1[i]] += 1
            s2_dict[s2[i]] += 1
        
        matches = 0
        
        for key in s1_dict:
            if s2_dict[key] == s1_dict[key]:
                matches += 1

        l = 0  
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            l_key = s2[l]
            s2_dict[l_key] -= 1
            if s2_dict[l_key] + 1 == s1_dict[l_key]:
                matches -= 1
            elif s2_dict[l_key] == s1_dict[l_key]:
                matches += 1
            l+=1
            r_key = s2[r]
            s2_dict[r_key] += 1
            if s2_dict[r_key] == s1_dict[r_key]:
                matches += 1
            elif s2_dict[r_key] - 1 == s1_dict[r_key]:
                matches -= 1
        return matches == 26

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
s1="adc"
s2="dcda"

print(solution.checkInclusion(s1, s2))
