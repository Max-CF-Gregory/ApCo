from matplotlib import pyplot as plt
from csv import DictReader
import numpy as np

listOfFiles = ["NHS_spending.csv"]
listOfHeaders = ["nominal terms £billions", "real terms £billions"]
sel = int(input("1. Line graph \n2. Line graph with delta \n3. Histogram \n"))
sel = 3

def getdata(filename: str) -> list[dict]: #
    with open(filename, "r") as f:
        reader = list(DictReader(f))
    return reader

ups = getdata(listOfFiles[0])

def linegraph():
    nompoints = [float(x.get(listOfHeaders[0])) for x in ups]
    realpoints = [float(x.get(listOfHeaders[1])) for x in ups]
    xpoints = [float((x.get("Year"))) for x in ups]
    plt.plot(xpoints, nompoints, label = listOfHeaders[0])
    plt.plot(xpoints, realpoints, label = listOfHeaders[1])
    return xpoints, nompoints, realpoints

def histgraph():
    nompoints = [float(x.get(listOfHeaders[0])) for x in ups]
    realpoints = [float(x.get(listOfHeaders[1])) for x in ups]
    xpoints = [float((x.get("Year"))) for x in ups]
    plt.hist([nompoints, realpoints], label = listOfHeaders, bins = 10)
    plt.xlabel("£billions")
if sel == 1:
    linegraph()
    plt.legend()
elif sel == 2:
    xpoints, nompoints, realpoints = linegraph()
    plt.fill_between(xpoints,nompoints , realpoints, color = "blue", alpha = 0.2)
    plt.legend()
elif sel == 3:
    histgraph()

plt.show()