import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///users_sqlalchemy2.db", echo=True)

# Dictionary keys MUST match column names exactly
users_dict = [
    {"first": "Joglul", "last": "Vuiya", "email": "jvuiya@gmail.com"},
    {"first": "Mofij", "last": "Khan", "email": "mkhan@yahoo.com"},
    {"first": "Bodrul", "last": "Alom", "email": "bal@bal.com"},
    {"first": "Gonju", "last": "Fokir", "email": "fokir420@gmail.com"},
    {"first": "Mojnu", "last": "Mia", "email": "loverboy@hotmail.com"}
]

metadata = sqlalchemy.MetaData()

# Table definition (names here must match dictionary keys)
users_table = sqlalchemy.Table("Users", metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first", sqlalchemy.Text),  # Note: "first"
    sqlalchemy.Column("last", sqlalchemy.Text),   # Note: "last"
    sqlalchemy.Column("email", sqlalchemy.Text))  # Note: "email"

# Create all tables
metadata.create_all(engine)

with engine.begin() as conn:
    # Insert data
    # conn.execute(sqlalchemy.insert(users_table), users_dict)  # Note: Removed .values()
    
    # Query data
    result = conn.execute(sqlalchemy.select(users_table.c.email))
    for row in result:
        print(row)