import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# Create Table
# cursor.execute('''CREATE TABLE IF NOT EXISTS Users 
#                (User_Id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                'First Name' TEXT,
#                'Last Name' TEXT,
#                'Email Address' TEXT)''')

# Insert 5 data
# users_list = [("Joglul","Vuiya", "jvuiya@gmail.com"),
#               ("Mofij","Khan", "mkhan@yahoo.com"),
#               ("Bodrul","Alom", "bal@bal.com"),
#               ("Gonju", "Fokir", "fokir420@gmail.com"),
#               ("Mojnu", "Mia", "loverboy@hotmail.com")]
# cursor.executemany('''INSERT INTO Users VALUES (NULL, ?,?,?)''',users_list)

# Retrieve all the users
cursor.execute('''SELECT [Email Address] FROM Users''')
print(cursor.fetchall())

connection.commit()
connection.close()