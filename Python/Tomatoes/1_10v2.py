import csv

datasets = ["Dr_Elders_Tomatoes.csv", "Mr_ONeills_Tomatoes.csv"] #Set datasets

def getdata(filename: str) -> list[dict]: #Read datasets
    with open(filename, "r") as f:
        reader2 = list(csv.DictReader(f))
    return reader2

#1 find tallest plant in each :P
# for i in datasets:
#     reader = getdata(i)
#     heights = []
#     for row in reader:
#         heights.append(float(row["height"]))
#     print(f"{i[:-4]}: {max(heights)}cm")

#2 find the tallest plant with a sunlight % < 0.65 in each dataset :P
# for i in datasets:
#     reader = getdata(i)
#     heights = []
#     for row in reader:
#         if float(row["sun"]) < 0.65:
#             heights.append(float(row["height"]))
#     print(f"{i[:-4]}: {max(heights)}cm")

#3
# for i in datasets:
#     reader = getdata(i)
#     weights = []
#     for row in reader:
#         if float(row["sun"]) < 0.70:
#             weights.append(float(row["avg_weight"]))
#     print(f"{i[:-4]}: {sum(weights)/len(weights)}g")

#4
# for i in datasets:
#     reader = getdata(i)
#     weights = []
#     for row in reader:
#         weights.append(float(row["avg_weight"]))
#     print(f"{i[:-4]} {sum(weights)/1000}kg")

#5
# for i in datasets:
#     weights = []
#     reader = getdata(i)
#     for row in reader:
#         if float(row["sun"]) > 0.70:
#             weights.append(float(row["avg_weight"]))
#     print(f"{i[:-4]}: {sum(weights)/len(weights)}g")

#6
# for i in datasets:
#     reader = getdata(i)
#     weights = []
#     for row in reader:
#         weights.append(float(row["avg_weight"]))
#     print(f"{i[:-4]}: {sum(weights) / 1000}kg")