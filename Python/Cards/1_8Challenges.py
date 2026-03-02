# placeholder = str(input())
# p2 = placeholder.split()
# for i in range(len(p2)):
#     if len(p2[i]) >= 5:
#         p2[i] = p2[i][::-1]
# placeholder = " ".join(p2)
# print(placeholder)

# placeholder = str(input())
# p2 = list(placeholder.lower())
# p3 = []
# for i in range(len(p2)):
#     if p2.count(p2[i]) > 1:
#         p3.append(p2[i])
#     if p2[i] in p3:
#         p2[i] = ")"
#     else:
#         p2[i] = "("
# placeholder = "".join(p2)
 # print(placeholder)

playercount = int(input())
playerdict = {}
roundcount = 0
trumpsuit = ""

for i in range(playercount):
    playerdict.update({f"Player{i}":[]})

print(playerdict.items())

with open("cards.txt", "r") as c:
    cr = c.readlines()
    for i in range(len(cr)):
        cr[i] = cr[i][:-1]
    print(cr)

def DealCards():
    pcounter = 0
    for i in range(5*playercount):
        pass

def PlayRound():
    plays = []
    trumpplays = []
    plays2 = []
    trumpplays2 = []
    for i in playercount():
        plays.append(playerdict[i][roundcount])
    for b in plays:
        if b[0] == trumpsuit:
            trumpplays.append(plays[i])
    if len(trumpplays) > 0:
        for c in trumpplays:
            trumpplays2.append(c[1:])
        for d in plays:
            if d == trumpplays.max():
                return d
    else:
        for e in plays:
            plays2.append(e[1:])
        for f in plays:
            if f == plays.max():
                return f

pass