from db_utilities import access_db

q = "FROM Words SELECT *;"
print(access_db(q))