"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def listDiagnosis():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    return diagnosis


def whatWeight():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    return weight_input


def weightAnalysis(weight):
    weight_data = weight.split(" ")
    weight = float(weight_data[0])
    print(weight)
    units = weight_data[1]
    if units == "lb":
        weightinKg = weight / 2.205
    return weightinKg


def calculate_Dosage(diagnosis, weight):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_first_day


def returnInfoTouser(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first \
            day".format(dosage_mg_first_day))

    return


if __name__ == '__main__':
    diag = listDiagnosis()
    weight = whatWeight()
    weight_in_kg = weightAnalysis(weight)
    dosage_per_Day = calculate_Dosage(diag, weight_in_kg)
    returnInfoTouser(weight_in_kg, dosage_per_Day)
