from matplotlib import pyplot as plt
#Dypaalu if the
from csv import DictReader
import numpy as np

listOfFiles = ["UK_public_spending.csv"]
listOfHeaders = ["benefits", "health", "education", "defence", "police", "transport", "housing", "aid"]

def getdata(filename: str) -> list[dict]: #
    with open(filename, "r") as f:
        reader = list(DictReader(f))
    return reader

ups = getdata(listOfFiles[0])

for i in range(len(listOfHeaders)):
    ypoints = [float(x.get(listOfHeaders[i])) for x in ups]
    xpoints = [float((x.get("year"))[0:4]) for x in ups]
    plt.plot(xpoints, ypoints, label = listOfHeaders[i])
plt.legend()
plt.show()