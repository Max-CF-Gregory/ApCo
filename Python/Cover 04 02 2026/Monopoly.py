def get_vals_from_file(f: str) -> list[str]:
    l1 = open(f, "r")
    l1 = l1.read()
    splitlist = l1.split("\n")
    return splitlist

def divide_rolls_by_player(all_rolls: list[str], player: int) -> list[str]:
    p1 = []
    p2 = []
    count = 0
    for i in range(len(all_rolls)):
        if count % 2 == 0:
            p1.append(all_rolls[i])
        else:
            p2.append(all_rolls[i])

        splitpair = all_rolls[i].split(" ")
        if splitpair[0] != splitpair[1]:
            count+=1
        else:
            pass
    if player == 1:
        return p1
    elif player == 2:
        return p2

def sum_rolls(player_rolls: list[str]) -> int:
    playersum = 0
    for i in range(len(player_rolls)):
        splitlist = player_rolls[i].split(" ")
        playersum+=int(splitlist[0])
        playersum+=int(splitlist[1])
    return playersum



l2 = get_vals_from_file("rolls.txt")
print(l2)
l3 = divide_rolls_by_player(l2, 1)
print(l3)
print(sum_rolls(l3))

#Name property
#Answer: Visiting Jail