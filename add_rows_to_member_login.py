import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

#data supplied as a tuple of tuples. ? - placeholder for data
sql = "insert into member_login values(?, ?, ?)"
data = ((1, "rachel", "vanlandingham"), (2, "ian", "lawson"))
cursor.executemany(sql, data)

#commit the changes
conn.commit()
conn.close()
