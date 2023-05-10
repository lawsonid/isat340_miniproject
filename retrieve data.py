import sqlite3

# create or connect to an existing database
conn = sqlite3.connect("celebrities.db")

# get a cursor to work with the database
cursor = conn.cursor()

# SQL SELECT statement to retrieve data from the members table
sql = "SELECT * FROM members"

# execute the SQL statement
cursor.execute(sql)

# fetch all the rows returned by the SQL statement
rows = cursor.fetchall()

# print the rows
for row in rows:
    print(row)

# close the connection to the database
conn.close()
