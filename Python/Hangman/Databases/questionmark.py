import sqlite3

query = """SELECT * FROM Players WHERE playerID = ?;"""

connection = sqlite3.connect("Hangman.db")
cursor = connection.cursor()

result = cursor.execute(query)
connection.commit()

if result != None:
    records = result.fetchall()

print(records)

connection.close()