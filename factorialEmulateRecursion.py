#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 16:53:15 2022

@author: michaellee
"""

callStack = [] # the expicit call stack, which holds "frame objects"
callStack.append({'returnAddr': 'start', 'number': 5}) # "call" the "factorial" function"
returnValue = None

while len(callStack) > 0:
    # the body of the "factorial() function"
    number = callStack[-1]['number']
    returnAddr = callStack[-1]['returnAddr']
    
    if returnAddr == 'start':
        if number == 1:
            # base case
            returnValue = 1
            callStack.pop() # "return" from "function call"
            continue
        else:
            # recursive case
            callStack[-1]['returnAddr'] = 'after recursive call'
            # "call" the "factorial()" function
            callStack.append({'returnAddr': 'start', 'number': number - 1})
            continue
    elif returnAddr == 'after recursive call':
        returnValue = number * returnValue
        callStack.pop() # return from function call
        continue

print(returnValue)