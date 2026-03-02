from matplotlib import pyplot as plt
from csv import DictReader
import numpy as np

listOfFiles = ["Dr_Elders_Tomatoes.csv", "Mr_ONeills_Tomatoes.csv"]

def getdata(filename: str) -> list[dict]: #Read datasets
    with open(filename, "r") as f:
        gdreader = list(DictReader(f))
    return gdreader

def variabibbles():
    vbmax1, vbmax2, vbmax3 = float(input(f"Input your maximum value for bucket 1 of {conj1}: ")), float(input(f"Input your maximum value for bucket 2 of {conj1}: ")), float(input(f"Input your maximum value for bucket 1 of {conj1}: "))
    return vbmax1, vbmax2, vbmax3

conj1, conj2 = input("Enter independent variable (height, avg_weight, sun, month): "), input("Enter dependent variable (height, avg_weight, sun): ")
bucket1, bucket2, bucket3 = [],[],[]

with open ("Dr_Elders_Tomatoes.csv") as csvfile:
    reader = DictReader(csvfile)
    if conj1 == "month": # Months
        for row in reader:
            if row["month"] == "April":
                bucket1.append(float(row[f"{conj2}"]))
            elif row["month"] == "May":
                bucket2.append(float(row[f"{conj2}"]))
            elif row["month"] == "June":
                bucket3.append(float(row[f"{conj2}"]))
        print(f"April: {sum(bucket1) / len(bucket1)}\nMay: {sum(bucket2) / len(bucket2)}\nJune: {sum(bucket3) / len(bucket3)}")

    else:
        max1, max2, max3 = variabibbles()
        for row in reader:
            if float(row[f"{conj1}"]) < max1:  # Bucket 1:55-65,Bucket 2:65:75,Bucket 3:75-85
                bucket1.append(float(row[f"{conj2}"]))
            elif max1 <= float(row[f"{conj1}"]) < max2:
                bucket2.append(float(row[f"{conj2}"]))
            elif max2 <= float(row[f"{conj1}"]) < max3:
                bucket3.append(float(row[f"{conj2}"]))
        print(f"Bucket 1: {sum(bucket1) / len(bucket1)}\nBucket 2: {sum(bucket2) / len(bucket2)}\nBucket 3: {sum(bucket3) / len(bucket3)}")