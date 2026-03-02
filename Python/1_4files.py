def NumKey(e):
    return e[-2]

# with open("fruit.txt", "r") as f:
#     fr = f.readlines()
#     for i in fr:
#         print(i)
#     fr.sort()
#     for i in fr:
#         print(i)
# with open("fruit.txt", "w") as g:
#     g.write("")
# with open("fruit.txt", "a") as g:
#     for i in fr:
#         g.write(i)

# with open("fruit2.txt", "r") as f:
#     fr = f.readlines()
#     for i in fr:
#         print(i[-2])

# with open("fruit2.txt", "r") as f:
#     fr = f.readlines()
#     fr.sort(key = NumKey)
# with open("fruit2.txt", "w") as g:
#     g.write("")
# with open("fruit2.txt", "a") as g:
#     for i in fr:
#         g.write(i)

def change_fruit_number(fruit: str, num: int):
    with open("fruit2.txt", "r") as t:
        tr = t.readlines()
        for i in range(len(tr)):
            if fruit in tr[i]:
                tr[i] = f"{fruit} {num}\n"
            else:
                pass
    with open("fruit2.txt", "w") as u:
        u.write("")
    with open("fruit2.txt", "a") as u:
        for i in tr:
            u.write(i)

change_fruit_number("Lemon", 6)