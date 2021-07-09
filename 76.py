# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:15:24 2021

76. Minimum Window Substring
"""


s = "ADOBECODEBANXXC"   
t = "ABC"

def minWindow(s,t):
    window = []
    for letter_s in s:
        if letter_s == t[0]:
            while letter_s not in window:
                window.append(letter_s)
        else:
             print(letter_s, window)
                
    return window

print(minWindow(s,t))
