#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:21:11 2023

@author: poojap
"""

import requests


# out_data = {"name": "Pooja Parameswaran", "net_id": "pkp14", "e-mail":
#             "pooja.parameswaran@duke.edu"}
# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
#                    json = out_data)
# print(r.status_code)
# print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)
