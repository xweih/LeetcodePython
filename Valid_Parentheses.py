# -*- coding: utf-8 -*-
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.
"""


def Valid_parentheses(s):
    
    ss=list(s)
    
    p=[ ['(', ')'], ['[', ']'], ['{', '}']]
    
    length=len(list(ss))
    
    if ((length % 2) != 0) or (length == 0):
        return False
    else: 
        while len(ss) > 0:
            if [ss[int(len(ss)/2)-1],ss[int(len(ss)/2)]] not in p:
                return False                
            else:
                ss.pop(int(len(ss)/2)-1)
                ss.pop(int(len(ss)/2))
                if len(ss)== 0: 
                    return True
                else:
                    continue

s = "()[]{}"

print(Valid_parentheses(s))