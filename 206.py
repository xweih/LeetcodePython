# -*- coding: utf-8 -*-
"""    
Created on Fri Jun 18 12:10:45 2021
h
206. Reverse Linked List    
"""


def reverselist(nums): 
    first = head
    if (not first) or (not first.next): return first

    first.next, curr, prev = None, first.next, first
        
    #1. Reverse  (curr.next = prev)
    #2. Update Current
    #3. Update previous
        
    while curr.next:
        curr.next, curr, prev = prev, curr.next, curr
        
    curr.next = prev
    return curr 

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
