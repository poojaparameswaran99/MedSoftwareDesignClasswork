#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:08:05 2023

@author: poojap
"""


def test_check_fever():
    input_temps = [97, 98.6, 100.1, 103, 98.4]
    answer = check_fever(input_temps)
    expected = True
    assert answer == expected


def check_fever(input_list):
    for temperature in input_list:
        if temperature < 100.5:
            return True
    return False
