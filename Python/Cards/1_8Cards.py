playercount = int(input())
playerdict = {}
roundcount = 0
trumpsuit = ""

for i in range(playercount): # Create dictionary for players
    playerdict.update({f"Player{i}":[]})

with open("cards.txt", "r") as c: # Create list of cards in deck
    cr = c.readlines()
    for i in range(len(cr)):
        cr[i] = cr[i][:-1]
    print(cr)

def DealCards():
    pcounter = 0
    for i in range(playercount*5):
        print(playerdict[f"Player{pcounter}"][0])
        if pcounter == playercount:
            pcounter = 0



print(playerdict["Player2"][0])