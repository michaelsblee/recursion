#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:06:48 2022

@author: michaellee
"""

def findSubstringIterative(needle, haystack):
    i = 0
    while i < len(haystack):
        if haystack[i:i + len(needle)] == needle:
            return i
        i += 1
    return -1

def findSubstringRecursive(needle, haystack, i=0):
    if i >= len(haystack):
        return -1
    if haystack[i:i + len(needle)] == needle:
        return i
    else:
        return findSubstringRecursive(needle, haystack, i + 1)
    
print(findSubstringIterative('cat', 'My cat Zophie'))
print(findSubstringRecursive('cat', 'My cat Zophie'))