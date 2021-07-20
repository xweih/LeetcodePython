# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:11:51 2021

3. Longest Substring Without Repeating Characters
"""


s = "afdsssafds"

def lengthOfLongestSubstring(s):
        longest_string = left = 0
        seen = {}
        
        for i, char in enumerate(s):
            if left <= seen.get(char, -1):
                left = seen[char] + 1
                print(i, char, left, seen, longest_string)
            else:
                longest_string = max(longest_string, i + 1 - left)               
                print(i, char, left, seen, longest_string)
                
            seen[char] = i
        return longest_string

print(lengthOfLongestSubstring(s))