import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

sql = "create table member_login(memberID integer PRIMARY KEY, username text, password text)"
cursor.execute(sql)

#commit the changes to the database
conn.commit()
conn.close()
