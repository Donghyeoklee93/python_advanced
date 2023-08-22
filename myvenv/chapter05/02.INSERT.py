# module
import sqlite3

# open database
conn = sqlite3.connect(
    "/Users/henry/Documents/python_advanced/myvenv/chapter05/SQL_DDL.db"
)

# create cursor
cur = conn.cursor()

# write sql
INSERT_SQL = "INSERT INTO item(code, name, price) VALUES (?, ?, ?);"

# Adding Multiple Data Entries at Once
data = (
    ("A00002", "air conditioner", 350000),
    ("A00003", "Latest Model Smartphone", 800000),
    ("A00004", "Cost-Effective Laptop", 650000),
)
# sql execution
cur.executemany(INSERT_SQL, data)

# commit
conn.commit()

# database close
conn.close()
