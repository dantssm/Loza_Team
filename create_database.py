"""creates a database for further usage"""
import sqlite3

def create_database():
    conn = sqlite3.connect("databse.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE users (
              user_id integer PRIMARY KEY,
              username text,
              email text,
              password text,
              note_color text
            )""")

    c.execute("""CREATE TABLE reviews (
              user_id integer,
              wine_id integer,
              review text,
              rating integer,

              foreign key (user_id) references users(user_id),
              foreign key (wine_id) references wines(wine_id)
            )""")

    c.execute(
        """CREATE TABLE friends (
              user_id integer,
              friend_id integer,
              
              foreign key (user_id) references users(user_id)
              foreign key (friend_id) references users(user_id)
            )"""
    )

    c.execute("""CREATE TABLE tasted_wines (
              user_id integer,
              wine_id integer,

              foreign key (user_id) references users(user_id)
              foreign key (wine_id) references wines(wine_id)
            )""")

    c.execute("""CREATE TABLE wines (
              wine_id integer PRIMARY KEY,
              name text,
              taste text,
              attribute text,
              color text,
              country text,
              glass text
            )""")

    c.execute("""CREATE TABLE wishlist (
              user_id integer,
              wine_id integer,

              foreign key (user_id) references users(user_id)
              foreign key (wine_id) references wines(wine_id)
            )""")

    c.execute("""CREATE TABLE snack (
              wine_id integer,
              snack text,

              foreign key (wine_id) references wines(wine_id)
            )""")

    c.execute("CREATE INDEX idx_user_id_reviews ON reviews(user_id)")
    c.execute("CREATE INDEX idx_wine_id_reviews ON reviews(wine_id)")
    c.execute("CREATE INDEX idx_user_id_friends ON friends(user_id)")
    c.execute("CREATE INDEX idx_user_id_tasted_wines ON tasted_wines(user_id)")
    c.execute("CREATE INDEX idx_user_id_wishlist ON wishlist(user_id)")

    c.execute("""INSERT INTO wines (name, taste, attribute, color, country) VALUES
              ('Solicello Merlot', 'fruity', 'dry', 'red', 'Italy'),
              ('Gaumen Spiel Gewurztraminer', 'herbs', 'semisweet', 'white', 'Germany')
              """)

    # c.execute("SELECT * FROM wines")
    # print(c.fetchall())

    conn.commit()
    conn.close()

