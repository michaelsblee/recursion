#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:38:12 2022

@author: michaellee
"""

def countDownAndUp(number):
    print(number)
    if number == 0:
        # base case
        print('Reached the base case.')
        return
    else:
        # recursive case
        countDownAndUp(number - 1)
        print(number, 'returning')
        return

countDownAndUp(3)