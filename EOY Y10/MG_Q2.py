def same_value(c1: int, c2: int)->bool:
    nc1 = c1%13
    nc2 = c2%13
    if nc1==nc2: return True
    else: return False

def read_file(filename: str) -> list[int]:
    nums = []
    with open(filename, "r") as f:
        strnums = f.readlines()
        for i in range(len(strnums)):
            nums.append(int(strnums[i].strip("\n")))
    return nums

#full implementation (Q4) starts here
allcards = read_file("EOY Y10/cards.txt")
acards, bcards = [], []
pile = []
count=-1
for i in range(len(allcards)):
    count+=1
    pile.append(allcards[i])
    if len(pile)>1:
        if same_value(pile[count], pile[count-1]):
            if allcards.index(max(pile[count], pile[count-1]))%2==0: acards.extend(pile)
            else: bcards.extend(pile)
            pile.clear()
            count = -1
    if i==len(allcards)-1:
        if allcards.index(max([pile[count], pile[count-1]]))%2==0: acards.extend(pile)
        else: bcards.extend(pile)
print(len(acards))
print(len(bcards))
if allcards.index(33)%2==0: print("7oH started in A's hand")
else: print("7oH started in B's hand")
if 33 in acards: print("7oH now in A's hand")
else: print("7oH now in B's hand")