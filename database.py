#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:18:16 2023

@author: poojap
"""

def create_patient_entry(patient_name, patient_mrn, patient_age):
    # List of Keys
    firstname, lastname = patient_name.split(" ")
    keyList = ["First Name", "Last Name", "MRN", "Age", "Tests"]
    new_patient = [firstname, lastname, patient_mrn, patient_age, []]
    # Using Dictionary comprehension
    patientdict = {key: None for key in keyList}
    for i, val in enumerate(new_patient):
        patientdict[keyList[i]] = val
    # print(patientdict)
    return patientdict


def get_full_name(dictionary):
    firstname = dictionary['First Name']
    lastname = dictionary["Last Name"]
    fullname = firstname +" " + lastname
    print(fullname)
    return fullname


def print_database(db):
    for patient in db.values():
        print ("\tMRN: {}, Full Name: {}, Age: {}".format(patient["MRN"], get_full_name(patient), patient["Age"]))


def main_driver():
    db = {}
    db [1] = (create_patient_entry("Ann Ables", 1, 34))
    db [2] = (create_patient_entry("Bob Boyles", 2, 45))
    db [3] = (create_patient_entry("Chris Chou", 3, 52))    
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "LDL", 100)
    add_test_to_patient(db, 3, "HDL", 99)
    print(db)
    print_database(db)
    # room_numbers = ["103", "232", "333"]
    
    # print_directory(db, room_numbers)
    gettestresult = get_test_result(db, 2, "LDL")
    print(gettestresult)
    return

def find_Test_val(db, mrn_to_find, testname):
    for patient in db:
        if patient[1] == mrn_to_find:
            if patient[3][0][0] == testname:
                return patient[3][0][1]        


def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))
        
    for patient, rn in zip(db, room_numbers):
        print("Patient {} is in room {}".format(patient[0], rn))
    return


def get_patient_entry(db, mrn_to_find):
    patient = db.get(mrn_to_find)
    if patient is None:
        return False
    return patient


def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient is False:
        print("Bad Entry")
    else:
       patient["Tests"].append([test_name, test_value])
    return


def get_test_value_from_test_list(test_list, test_name):
    for test in test_list:
        if test[0] == test_name:
            return test[1]
    return False

def get_test_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_value = get_test_value_from_test_list(patient["Tests"], test_name)
    return test_value


if __name__ == "__main__":
    main_driver()
    