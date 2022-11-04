#! /usr/bin/env /usr/bin/python3
# Enters data into  a SQLITE database
db='database.db'
import sqlite3

# Establish a connection to the database
con=sqlite3.connect(db)

# Create a cursor object
cur=con.cursor()

# Add these new rows:
new_data = [
  ('100.100.120.201', 'a.b.c', 100),
  ('200.200.220.101', 'd.e.f', 200)
]

# Insert these new data into the table
cur.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_data)
con.commit

# Retrieve and print out the entire table
cur.execute("SELECT * FROM 'ips'")
print(cur.fetchall())