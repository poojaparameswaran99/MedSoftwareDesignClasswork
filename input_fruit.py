#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:03:01 2023

@author: poojap
"""

in_file = open("input_data.txt", "r")
fruits = in_file.readlines()
print(fruits)
in_file.close()
print(fruits)

in_file = open("input_data.txt", "r")

for line in in_file:
    print(line)

first_fruit = in_file.readline()
second_fruit = in_file.readline()
