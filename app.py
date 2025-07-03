import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()
# Create table
# cursor.execute('''CREATE TABLE IF NOT EXISTS Movies 
#                (Title TEXT, Director TEXT, Year INT)''')

# Insert a value
# cursor.execute('''INSERT INTO Movies VALUES
#                ('Taxi Driver', 'Martin Scorsese', 1976)''')

# Insert multiple values
# famousFilms = [
#               ('Pulp Fiction', 'Quentin Tarantino', 1994),
#               ('Back to the Future', 'Robert Zemeckis', 1985),
#               ('Moonrise Kingdom', 'Wes Anderson', 2012)]

# cursor.executemany('''INSERT INTO Movies VALUES (?, ?, ?)''', famousFilms)

# Retrieve all the values
# cursor.execute('''SELECT * FROM Movies''')
# print(cursor.fetchone())
# print(cursor.fetchall())

# Retrieve value using filter
release_year = (1985,)
cursor.execute('''SELECT * FROM Movies WHERE year=?''', release_year)
print(cursor.fetchone())


connection.commit()
connection.close()