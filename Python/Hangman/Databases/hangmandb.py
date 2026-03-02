import sqlite3

def access_db(q:str, write_query=True):
    connection = sqlite3.connect("hangman.db")
    cur = connection.cursor()
    try:
        if write_query:
            res = cur.execute(q)
            connection.commit()
        else:
            res = cur.execute(q).fetchall()
            connection.close()
            return res
    except:
        print("Query execution failed")
        connection.close()

access_db("""SELECT * FROM Players;""", write_query=False)