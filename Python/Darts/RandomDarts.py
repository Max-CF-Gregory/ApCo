import random
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 25, 50]
d1 = {"Max":[501,0], "Anouska":[501,0]}

players = list(d1.keys())
winner = None
throw = 0

while not winner:
    for player in players:
        for _ in range(3):
            if throw >= len(l1):
                pass
            score, turns = d1[player]
            throw_value = random.choice(l1)
            print(throw_value)
            if score - throw_value < 0:
                d1[player][1] += 1
            else:
                d1[player][0] -= throw_value
                d1[player][1] += 1
                if d1[player][0] == 0:
                    winner = player
                    break
            throw += 1
        if winner:
            break

print(f"{winner if winner else 'Noone'} is victorious")

with open("games_played.txt", "w") as f:
    printlist = [f"Max got to {d1["Max"][0]} with {d1["Max"][1]} throws. ", f"\nAnouska got to {d1["Anouska"][0]} with {d1['Anouska'][1]} throws. ", f"\n{winner} won."]
    f.writelines(printlist)