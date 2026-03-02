list_1 = ["a", "b", "c", "d", "e"]
list_2 = [3, 3, 7, 9, 4]

dict_1 = {}
for i in range(len(list_1)):
    dict_1.update({list_1[i]:list_2[i]})
print(dict_1)

dict_2 = {}
for i in range(len(list_1)):
    dict_2.update({list_2[i]:list_1[i]})
print(dict_2)