#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:45:13 2023

@author: poojap
"""

import requests

r_get = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/pkp14")
print(r_get.text)

rgetDonor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M8")

rgetRecipient = requests.get("http://vcm-7631.vm.duke.edu:5002/"
                             "get_blood_type/M5")

print(rgetDonor.text)
print(rgetRecipient.text)
# NO! B+ cannot recieve from AB-

out_data = {"Name": "pkp14", "Match": "No"}
rpost = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                      json=out_data)
print(rpost.text)
