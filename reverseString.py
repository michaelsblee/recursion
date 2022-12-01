#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 10:16:21 2022

@author: michaellee
"""

def rev(theString):
    if len(theString) == 0 or len(theString) == 1:
        # base case
        return theString
    else:
        # recursive case
        head = theString[0]
        tail = theString[1:]
        return rev(tail) + head
    
print(rev('abcdef'))
print(rev(''))
print(rev('X'))