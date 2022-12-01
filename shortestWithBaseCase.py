#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 06:08:03 2022

@author: michaellee
"""

def shortestWithBaseCase(makeRecursiveCall):
    print('shortestWithBaseCase(%s) called.' % makeRecursiveCall)
    if not makeRecursiveCall:
        # BASE CASE
        print('Returning from base case.')
        return
    else:
        # RECURSIVE CASE
        shortestWithBaseCase(False)
        print('Returning from recursive case.')
        return

print('Calling shortestWithBaseCase(False):')   
shortestWithBaseCase(False)
print()
print('Calling shortestWithBaseCase(True):')
shortestWithBaseCase(True)