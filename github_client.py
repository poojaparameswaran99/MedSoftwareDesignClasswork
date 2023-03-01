#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:10:28 2023

@author: poojap
"""


import requests

r = requests.get("https://api.github.com/repos/poojaparameswaran99/"
                 "MedSoftwareDesignClasswork/branches")
print(r)
print(type(r))
print(r.status_code)
# print(r.text)
branches = r.json()
print(branches)
for branch in branches:
    print(branch["name"])
