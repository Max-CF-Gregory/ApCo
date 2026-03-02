import csv
import random

def guess(unfinishedWord:list[str], lives:int, guesses:list[str]) -> tuple[list[str], int, list[str]]:
    pass

def get_word(filename: str) -> str:
    with open(filename, "r") as f:
        reader = list(csv.DictReader(f))
        if len(reader) < 1:
            return f"no words found in {filename}"
        num = random.randint(0, len(reader)-1)
        word = str(reader[num]["word"])
    return word.lower()