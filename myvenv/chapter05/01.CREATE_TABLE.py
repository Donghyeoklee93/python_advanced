# module
import sqlite3

# open database
conn = sqlite3.connect(
    "/Users/henry/Documents/python_advanced/myvenv/chapter05/SQL_DDL.db"
)

# create cursor
cur = conn.cursor()

# write sql
CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS Item(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
"""

# sql execution
cur.execute(CREATE_SQL)

# database close
conn.close()
