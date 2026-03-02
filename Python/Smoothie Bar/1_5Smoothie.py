s, c = 0, 0
St, Or, Le, Ra, Me = 0.0, 0.0, 0.0, 0.0, 0.0
ingredientList = []

def getIngredients(s, c, St, Or, Le, Ra, Me):
    for i in range(s):
        Ra -= 4
        St -= 3
        Or -= 1
    for i in range(c):
        Le -= 1
        Me -= 0.5
        Or -= 2
    return St, Or, Le, Ra, Me


with open("smoothie_order.txt", "r") as od:
    odr = od.readlines()
    for i in odr:
        if "Summer" in i:
            ri = i[-2]
            s += int(ri)
        elif "Citrus" in i:
            ri = i[-1]
            c += int(ri)

with open("smoothie_bar_stock.txt", "r") as bs:
    bsr = bs.readlines()
    for i in bsr:
        if "Strawberry" in i:
            St = int((i[0:-1].split(" "))[1])
        elif "Orange" in i:
            Or = int((i[0:-1].split(" "))[1])
        elif "Lemon" in i:
            Le = int((i[0:-1].split(" "))[1])
        elif "Raspberry" in i:
            Ra = int((i[0:-1].split(" "))[1])
        elif "Melon" in i:
            Me = int((i[0:-1].split(" "))[1])

St, Or, Le, Ra, Me = getIngredients(s, c, St, Or, Le, Ra, Me)
newIngredients = [St, Or, Le, Ra, Me]
replaceIngredients = []
for i in newIngredients:
    replaceIngredients.append(f"")