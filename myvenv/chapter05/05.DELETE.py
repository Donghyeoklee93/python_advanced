# module
import sqlite3

# open database
conn = sqlite3.connect(
    "/Users/henry/Documents/python_advanced/myvenv/chapter05/SQL_DDL.db"
)

# create cursor
cur = conn.cursor()

# write sql
DELETE_SQL = "DELETE FROM Item WHERE code='A00002'"

# sql execution
cur.execute(DELETE_SQL)

# commit
conn.commit()

# database close
conn.close()
