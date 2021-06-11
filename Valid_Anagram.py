# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:04:50 2021

Given two strings s and t , write a function to determine if t is an anagram of s.

"""


s = "rat"
t = "car"

list(s)

s1=sorted(list(s))

s1[2]

def anagram(s,t):
    
    return sorted(list(s))==sorted(list(t))   


print(anagram(s,t))