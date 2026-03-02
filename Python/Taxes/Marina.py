from matplotlib import pyplot as plt
from csv import DictReader
import numpy as np
import csv

headers = ["benefits", "health", "education", "defence", "police", "transport", "housing", "aid"]

def getdata(filename: str) -> list[dict]: # We covered this construct in class (1_11)
    with open(filename, "r") as f:
        reader = list(DictReader(f))
    return reader

ups = getdata("UK_public_spending.csv") #ups = UK Public Spending

with open("UK_public_spending.csv", "w") as f:
    for i in range(len(headers)):
        for x in range(len(ups)):
            if ups[x][headers(i)] == "--":
                ups[x][headers(i)] = "0"

# for i in range(len(headers)):
#     ypoints = [float(x.get(headers[i])) for x in ups] # Uses the list comprehension we learned
#     xpoints = [float((x.get("year"))[0:4]) for x in ups]
#     plt.plot(xpoints, ypoints, label = headers[i])

# plt.legend()
# plt.show()

print(ups)