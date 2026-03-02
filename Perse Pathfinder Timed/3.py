l1 = str(input())
l1 = l1.split(",")
for i in range(len(l1)):
    if ":=" in l1[i][1:2]:
        s1 = str(l1[i])
        print(s1[0])