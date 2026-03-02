import csv
import random

def get_word(filename:str):
    with open(filename, "r") as f:
        reader = list(csv.DictReader(f))
        num = random.randint(1, len(reader)-1)
        word = str(reader[num]["word"])
    return word.lower()


def guess(unfinishedword:str, lives:int, guesses:list[str]):
    guessin = input("Add your input")[0]
    if guessin in guesses:
        print("You have already guessed that letter, try again")
        guessin = input("Add your input")[0]
    if guessin in secret:
        for i in range(len(unfinishedword)):
            if secret[i] == guessin:
                unfinishedword[i] = guessin
            else:
                pass
    else:
        lives-=1
    guesses.append(guessin)
    print(unfinishedword)
    return unfinishedword, lives, guesses

secret = get_word("placeholder.csv")
uw = ["_" for _ in range(len(secret))]
l = 6
g = [""]
print(uw)
while True:
    uw, l, g = guess(uw, l, g)
    if "_" not in uw:
        print("You win!")
        quit()
    elif l == 0:
        print("You lose!")
        quit()