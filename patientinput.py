#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:33:29 2023

@author: poojap
"""

def read_file(filename):
    in_file = open(filename, "r")
    first_line = in_file.readline()
    patient_data = first_line.strip("\n").split("-")
    patient_id = int(patient_data[1])
    return patient_id

def test_read_file():
    import read_file
    filename = "my_test_data.txt"
    answer = read_file(filename)
    expected = 50