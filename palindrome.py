#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 10:32:37 2022

@author: michaellee
"""

def isPalindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        return True
    else:
        head = theString[0]
        middle = theString[1:-1]
        last = theString[-1]
        return head == last and isPalindrome(middle)
    
text = 'racecar'
print(str(isPalindrome(text)))