#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:32:26 2023

@author: poojap
"""

import requests

out_data = {"user": "PoojaParameswaran", "message": "Hi anusha whats up! ><)"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=out_data)
print(r)
r_in = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/ak701")
print(r_in.text)
