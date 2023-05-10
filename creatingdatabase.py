#import the built in sqlite3 module
import sqlite3
#create or connect to an existing database
conn = sqlite3.connect("celebrities.db")
#get a cursor to work with the database
cursor = conn.cursor()
sql = "create table celebs(celebID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, photo text, bio text)"
cursor.execute(sql)
#close connection to the database
#commit changes to the databse
conn.commit()
#Insert data into celebs table
sql = "insert into celebs values (?, ?, ?, ?, ?, ?, ?)"
data = ((1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402021/aj.jpg", "Angelina Jolie is an American actress, filmmaker, and humanitarian."),
        (2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402021/bp.jpg", "William Bradley pitt is an American actor and film producer."),
        (3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402021/sw.jpg", "Snow White is a Disney Princess."),
        (4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402021/dv.jpg", "Darth Vader is a villain in the Star Wars Movie Franchise."),
        (5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402021/ts.jpg", "Taylor Swift is an American singer-songwriter."),
        (6, "Byonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402021/bk.jpg", "Beyonce Knowles-Carter is an American singer, songwriter, record producer, dancer, and actress married to Jay-Z."),
        (7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402021/sg.jpg", "Selena Gomez is an American singer, actress, producer, and businesswoman."),
        (8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402021/sc.jpg", "Stephen Curry II is an American professional basketball player for the Golden State Warriors of the NBA."))

cursor.executemany(sql,data)
conn.commit()
#create members table
sql = "create table members(memberID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, bio text)"
cursor.execute(sql)
conn.commit()

#Insert data into members table
sql = "insert into members values (?, ?, ?, ?, ?, ?)"
data = ((1, "Rachel", "Vanlandingham", 20, "vanlanre@dukes.jmu.edu", "I was born and raised in northern Virginia."),
        (2, "Ian", "Lawson", 23, "lawsonid@dukes.jmu.edu", "I was born and raised in Waynesboro, Virginia"))
cursor.executemany(sql,data)
conn.commit()
conn.close()
