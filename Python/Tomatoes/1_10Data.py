import csv

#1 find tallest plant in each :P
# with open ("Dr_Elders_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     heights = []
#     for row in reader:
#         heights.append(float(row["height"]))
#     print(f"DET: {max(heights)}")
# with open ("Mr_ONeills_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     heights = []
#     for row in reader:
#         heights.append(float(row["height"]))
#     print(f"MOT: {max(heights)}")

#2 find the tallest plant with a sunlight % < 0.65 in each dataset :P
# with open ("Dr_Elders_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     heights = []
#     for row in reader:
#         if float(row["sun"]) < 0.65:
#             heights.append(float(row["height"]))
#     print(f"DET: {max(heights)}")
# with open ("Mr_ONeills_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     heights = []
#     for row in reader:
#         if float(row["sun"]) < 0.65:
#             heights.append(float(row["height"]))
#     print(f"MOT: {max(heights)}")

#3
# with open ("Dr_Elders_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     weights = []
#     for row in reader:
#         if float(row["sun"]) < 0.70:
#             weights.append(float(row["avg_weight"]))
#     print(f"DET: {sum(weights)/len(weights)}")
# with open ("Mr_ONeills_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     w = []
#     for row in reader:
#         if float(row["sun"]) < 0.70:
#             weights.append(float(row["avg_weight"]))
#     print(f"MOT: {sum(weights)/len(weights)}")

#4
# with open ("Dr_Elders_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     weights = []
#     for row in reader:
#         weights.append(float(row["avg_weight"]))
# with open ("Mr_ONeills_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         weights.append(float(row["avg_weight"]))
#     print(f"{sum(weights)/1000}kg")

#5
# with open ("Dr_Elders_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     weights = []
#     for row in reader:
#         if float(row["sun"]) > 0.70:
#             weights.append(float(row["avg_weight"]))
# with open ("Mr_ONeills_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         if float(row["sun"]) > 0.70:
#             weights.append(float(row["avg_weight"]))
#     print(f"{sum(weights)/len(weights)}g")

#6
# with open ("Dr_Elders_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     weights = []
#     for row in reader:
#         weights.append(float(row["avg_weight"]))
#     print(f"DET: {sum(weights) / 1000}kg")
# with open ("Mr_ONeills_Tomatoes.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     weights = []
#     for row in reader:
#         weights.append(float(row["avg_weight"]))
#     print(f"MOT: {sum(weights)/1000}kg")