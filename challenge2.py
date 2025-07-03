import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///users_sqlalchemy.db", echo=True)

users_dict = [
    {"first": "Joglul", "last": "Vuiya", "email": "jvuiya@gmail.com"},
    {"first": "Mofij", "last": "Khan", "email": "mkhan@yahoo.com"},
    {"first": "Bodrul", "last": "Alom", "email": "bal@bal.com"},
    {"first": "Gonju", "last": "Fokir", "email": "fokir420@gmail.com"},
    {"first": "Mojnu", "last": "Mia", "email": "loverboy@hotmail.com"}
]

with engine.connect() as conn:
  # conn.execute(
  #   sqlalchemy.text("CREATE TABLE IF NOT EXISTS Users " \
  #   "(user_id INTEGER PRIMARY KEY AUTOINCREMENT," \
  #   "first_name TEXT," \
  #   "last_name TEXT," \
  #   "email_address TEXT)")
  # )
  # conn.execute(
  #   sqlalchemy.text("INSERT INTO Users VALUES (NULL, :first, :last, :email)"),
  #   users_dict
  #   )
  # conn.commit()
  result = conn.execute(
    sqlalchemy.text("SELECT email_address FROM Users")
  )
  for row in result:
    print(row)