# module
import sqlite3

# open database
conn = sqlite3.connect(
    "/Users/henry/Documents/python_advanced/myvenv/chapter05/SQL_DDL.db"
)

# create cursor
cur = conn.cursor()

# write sql
SELECT_SQL = "SELECT * FROM item WHERE code = 'A00002'"

# sql execution
cur.execute(SELECT_SQL)

rows = cur.fetchall()
for row in rows:
    print(row)

# database close
conn.close()
