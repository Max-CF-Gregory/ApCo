from csv import DictReader
import random
import sqlite3
from typing import Any

connection = sqlite3.connect('Players.db')
cursor = connection.cursor()

def access_db(q:str, write_query=False):
    connection = sqlite3.connect("Hangman.db")
    cur = connection.cursor()
    try:
        if write_query:
            res = cur.execute(q)
            connection.commit()
        else:
            res = cur.execute(q).fetchall()
            return res
    except:
        print("query failed")
        connection.close()

def get_word(filename: str) -> str:
    file_type = filename.find(".")
    with open(filename, "r") as f:

        if filename[file_type:] == ".csv":
            reader = list(DictReader(f))
            if len(reader) < 1:
                return f"no words found in {filename}"
            else:
                number = random.randint(1, len(reader) - 1)
                word = str(reader[number]['word'])
            return word
        elif filename[file_type:] == ".db":
            playerID = int(input("PlayerID: "))
            rating = get_player_rating(playerID)
            if rating > -1:
                return random.choice(get_stretch_words(rating))

def get_player_rating(playerID: int) -> int:
    query = f"SELECT rating FROM Players WHERE playerID ='{playerID}';"

    connection = sqlite3.connect('Hangman.db')
    cursor = connection.cursor()

    result = cursor.execute(query)
    records = result.fetchall()

    if records:
        connection.close()
        return records[0][0]

    connection.close()
    return -1

def get_stretch_words(rating: int) -> list[str]:
    # gets words where ave_guesses
    words = []
    query = f"SELECT word FROM Words WHERE ave_guesses < {rating + 2} AND ave_guesses > {rating - 2};"

    connection = sqlite3.connect('Hangman.db')
    cursor = connection.cursor()

    result = cursor.execute(query)
    records = result.fetchall()
    for record in records:
        words.append(record[0])
    connection.close()
    return words

def new_record_values(lives:int, attempts:int, correct:int, ave_guesses:float):
    hig = attempts * ave_guesses
    attempts+=1
    correct+=1 if lives > 0 else correct
    hig+=lives
    ave_guesses = hig/attempts
    return attempts, correct, ave_guesses

def update_table(table_name: str, update_fields: list[str], update_vals: list[Any], target_field: str, target_val: Any) -> None:
        if type(target_val) == str:
            target_val = "'" + target_val + "'"
        field_vals = ""
        for i in range(len(update_fields)):
            if type(update_vals[i]) == str:
                update_vals[i] = "'" + update_vals[i] + "'"
            field_vals += update_fields[i] + "=" + str(update_vals[i]) + ", "
        field_vals = field_vals[:-2]

        query = f"UPDATE {table_name} SET {field_vals} WHERE {target_field} = {target_val};"
        access_db(query, write_query=True)
        return

def update_manager(table, fields, target_field, target_val):
    new_vals = new_record_values(10, 3, 3, 7.0)
    update_table(table, fields, list(new_vals), target_field, target_val)

t = "Words"
uf = ["attempts", "correct", "ave_guesses"]
vals = [6,5,5.0]
tf = "word"
tv = "goodbye"

update_manager(t, uf, tf, tv)

q2 = "SELECT * FROM Words;"
print(access_db(q2, write_query=False))