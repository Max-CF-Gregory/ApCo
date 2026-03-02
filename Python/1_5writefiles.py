with open("fruit.txt", "a") as f:
    f.writelines(["Tomato\n", "Plum\n", "Grapes\n"])

# quants = []
# overwrite = []
# with open("fruit.txt", "r") as f:
#     fr = f.readlines()
#     for i in range(len(fr)):
#         fr[i] = fr[i][0:-1]
#     for i in fr:
#         quants.append(int(input(f"Quantity for {i}:")))
#     for i in range(len(fr)):
#         overwrite.append(f"{fr[i]} {quants[i]}\n")
# with open("fruit.txt", "w") as f:
#     f.writelines(overwrite)

infr = False
fruit_name = str(input("Fruit name: "))
with open("fruit.txt", "r") as f:
    fr = f.readlines()
    for i in fr:
        if fruit_name in i:
            fr.remove(i)
            infr = True
            print(f"Eating a {fruit_name}")
    if infr == False:
        print(f"No {fruit_name} found")
with open("fruit.txt", "w") as f:
    f.writelines(fr)