import sqlite3
from typing import Any

def access_db(q:str, write_query=False):
    """connects to db and executes query. Read queries by defaut. Write queries should
    change default value of kwarg to True"""
    #IMPORTANT: insert the relative path from the main class of the project
    connection = sqlite3.connect('Hangman.db')
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
        print("query failed to execute")
        connection.close()