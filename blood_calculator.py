#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:28:59 2023

@author: poojap
"""

def interface():
    print("Blood calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Cholesterol")
        print("9 - Quit")
        choice = input("Select an option: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        # elif choice == "3":
        #     chol_driver():
        print("Program ending \n" )
        


        
def HDL_driver():
    HDL_in = HDL_input()
    HDL_analy = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analy)
    

def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40<= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def HDL_input():
    HDL_value = input("Enter the HDL result:")
    HDL_value= int(HDL_value)
    return HDL_value

def HDL_output(HDL_value, HDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value, HDL_analy))
    return


# Working on LDL

def LDL_analysis(LDL_int):
    if LDL_int < 130:
        ldlanswer = "Normal"
    elif 130 <= LDL_int <= 159:
        ldlanswer = "Borderline High"
    elif 160 <= LDL_int <= 189:
        ldlanswer = "High"
    else:
        ldlanswer = "Very High!"
    return ldlanswer

def LDL_driver():
    LDL_in = LDL_input()
    LDL_analy = LDL_analysis(LDL_in)
    LDL_output(LDL_in, LDL_analy)
    
def LDL_input():
    LDL_val = input("Enter LDL result: ")
    LDL_val = int(LDL_val)
    return LDL_val

def LDL_output(LDL_val, ldlanswer):
    print("The LDL result {} is considered {}".format(LDL_val, ldlanswer))
    return
    
# Analyzing Cholesterol levels
def total_cholesterol(cholest_int):
    if cholest_int < 200:
        cholanswer = "Normal"
    elif 200 <= cholest_int <239:
        cholanswer = "Borderline High"
    else:
        cholanswer = "High"
    return cholanswer


def cholesterol_input():
    chol_val = input("Enter Cholesterol result: ")
    chol_val = int(chol_val)
    return chol_val

interface()
