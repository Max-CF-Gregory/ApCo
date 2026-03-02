l1 = [8, 20, 20, 3, 8, 9, 8, 16, 7, 11, 8, 10, 13, 57, 18, 16, 12, 6, 6, 14, 13, 20, 38, 1, 5, 8, 7, 13, 12, 15, 10, 5, 7, 20, 8, 10, 20, 14, 12, 17, 2, 2, 12, 6, 18, 11, 4, 10, 7, 8, 42, 24, 20, 14, 6, 14, 48, 9, 20, 2, 12, 6, 60, 18, 2, 24, 34]
d1 = {input("Enter Player 1 Name:"):[501,0], input("Enter Player 1 Name:"):[501,0]}
player = -1


players = list(d1.keys())
winner = 0

throw = 0

while throw < len(l1) and winner != 1:
    for player in players:
        for i in range(3):
            if throw >= len(l1):
                break
            score, playerthrow = d1[player]
            throw_value = l1[throw]
            if score - throw_value < 0:
                d1[player][1] += 1
                throw += 1
                continue
            d1[player][0] -= throw_value
            d1[player][1] += 1
            throw += 1
            if d1[player][0] == 0:
                winner = player
                break
        if winner:
            break
if winner:
    print(f"{winner} is victorious")
else:
    winner = "Noone"
    print("Noone won")
