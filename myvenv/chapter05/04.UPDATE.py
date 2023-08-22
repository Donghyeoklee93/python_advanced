# module
import sqlite3

# open database
conn = sqlite3.connect(
    "/Users/henry/Documents/python_advanced/myvenv/chapter05/SQL_DDL.db"
)

# create cursor
cur = conn.cursor()

# write sql
UPDATE_SQL = "UPDATE Item set price = 650000 WHERE code='A00002'"

# sql execution
cur.execute(UPDATE_SQL)

# commit
conn.commit()

# database close
conn.close()
