import random
l1 = []
d1 = {"Max":[501,0], "Anouska":[501,0]}

players = list(d1.keys())
winner = None
throw = 0

def throwcalc():
    selector = random.randint(1,5)
    if selector in [1,2,3]: return random.randint(1,20)
    elif selector == 4: return (random.randint(1,20))*2
    elif selector == 5: return (random.randint(1,20))*3

l1.append(throwcalc())

while throw < len(l1) and not winner:
    for player in players:
        for _ in range(3):
            if throw >= len(l1):
                break
            score, turns = d1[player]
            throw_value = l1[throw]
            if score - throw_value < 0:
                d1[player][1] += 1
            else:
                d1[player][0] -= throw_value
                d1[player][1] += 1
                if d1[player][0] == 0:
                    winner = player
                    break
            l1.append(throwcalc())
            throw += 1
        if winner:
            break

print(f"{winner if winner else 'Noone'} is victorious")

with open("games_played.txt", "w") as f:
    printlist = [f"Max got to {d1["Max"][0]} with {d1["Max"][1]} throws. ", f"\nAnouska got to {d1["Anouska"][0]} with {d1['Anouska'][1]} throws. ", f"\n{winner} won."]
    f.writelines(printlist)