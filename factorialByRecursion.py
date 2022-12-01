#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:52:19 2022

@author: michaellee
"""
#from showcallstack import showcallstack
def factorial(number):
#    showcallstack()
    if number == 1:
        # base case
        return 1
    else:
        # recursive case
        return number * factorial(number - 1)
    # showcallstack()
print(factorial(5))