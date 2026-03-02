from matplotlib import pyplot as plt
from csv import DictReader
import numpy as np

listOfFiles = ["Dr_Elders_Tomatoes.csv", "Mr_ONeills_Tomatoes.csv"]

def getdata(filename: str) -> list[dict]: #Read datasets
    with open(filename, "r") as f:
        reader = list(DictReader(f))
    return reader

dataPoint = input("Enter independent variable: ")

det = getdata(listOfFiles[0])
mot = getdata(listOfFiles[1])

detData = [float(x.get(dataPoint)) for x in det]
motData = [float(x.get(dataPoint)) for x in mot]
# diffData = [detData[x]-motData[x] for x in range(len(detData))]

lBin = min(zip(detData, motData))[0]
uBin = max(zip(detData, motData))[0]
bins = np.linspace(lBin, uBin, 5)

plt.hist(detData, bins=bins+3, color="b", edgecolor="black", rwidth=0.3, align="mid", alpha=0.7)
plt.hist(motData, bins=bins-3, color="r", edgecolor="black", rwidth=0.3, align="mid", alpha=0.7)
plt.xlabel(f"{dataPoint}")
plt.ylabel("frequency")
plt.show()