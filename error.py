#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:45:54 2023

@author: poojap
"""

import math

def calc_square_root(n):
    try:
        from my_calculator import sqrt
   except ModuleNotFoundError:
       from math import sqrt
   answer = sqrt(n)
   return answer


def squareroot(lst):
    newlist = []
    for i in lst:
        try:
            val = math.sqrt(i)
        except ValueError:
            i = abs(i)
            val = math.sqrt(i)
        newlist.append(val)
    return newlist


def main():
    print(calc_square_root(3))
    print(squareroot([1, -1, 2, -2, 3, -3]))


if __name__ == "__main__":
    main()
