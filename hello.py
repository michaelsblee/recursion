#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:03:41 2022

@author: michaellee
"""

print('Code in a loop:')
i = 0
while i < 5:
    print(i, 'Hello, world!')
    i += 1

print('Code in a function:')
def hello(i = 0):
    print(i, 'Hello, world!')
    i += 1
    if i < 5:
        hello(i)
    else:
        return
hello()