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
        print("9 - Quit")
        choice = input("Select an option:")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        print("Program ending")
        



interface()
