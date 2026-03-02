import csv

bucket1 = []
bucket2 = []
bucket3 = []
max1, max2, max3 = float(input("Enter max for bucket 1: ")), float(input("Enter max for bucket 2: ")), float(input("Enter max for bucket 3: "))



with open("Dr_Elders_Tomatoes.csv") as csvfile: #Conjecture: Higher light means greater height
    reader = csv.DictReader(csvfile)
    for row in reader:
        if float(row["sun"]) < max1: #Bucket 1:55-65,Bucket 2:65:75,Bucket 3:75-85
            bucket1.append(float(row["height"]))
        elif max1 <= float(row["sun"]) < max2:
            bucket2.append(float(row["height"]))
        elif max2 <= float(row["sun"]) < max3:
            bucket3.append(float(row["height"]))
print(f"Bucket 1: {sum(bucket1)/len(bucket1)}\nBucket 2: {sum(bucket2)/len(bucket2)}\nBucket 3: {sum(bucket3)/len(bucket3)}")