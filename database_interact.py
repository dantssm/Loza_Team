import sqlite3
from python_classes.user import User
from python_classes.wine import Wine

conn = sqlite3.connect("databse.db")
c = conn.cursor()

def add_new_user(user:User):
    with conn:
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                  (user.username, user._User__email, user._User__password))
        
def del_user(user:User):
    with conn:
        c.execute("DELETE FROM users WHERE user_id = ?",
                  (user.id))
        # more???

def set_note_color(user:User, color):
    with conn:
        c.execute("UPDATE users SET note_color = ? WHERE user_id = ?", 
                  (color, user.id))
        
def change_username(user:User, new_name):
    with conn:
        c.execute("UPDATE users SET username = ? WHERE user_id = ?",
                  (new_name, user.id))
        
def add_review(user:User, wine:Wine, text, rating):
    with conn:
        c.execute("INSERT INTO reviews (user_id, wine_id, review, rating) VALUES (?, ?, ?, ?)",
                  (user.id, wine.id, text, rating))
        
def del_review(user:User, wine:Wine):
    with conn:
        c.execute("DELETE FROM reviews WHERE user_id = ? and wine_id = ?",
                  (user.id, wine.id))

def add_friend(user1:User, user2:User):
    with conn:
        c.execute("INSERT INTO friends (user_id, friend_id) VALUES (?, ?)",
                  (user1.id, user2.id))
        c.execute("INSERT INTO friends (user_id, friend_id) VALUES (?, ?)",
            (user2.id, user1.id))
        
def add_wine_to_wishlist(user:User, wine:Wine):
    with conn:
        c.execute("INSERT INTO wishlist (user_id, wine_id) VALUES (?, ?)",
                  (user.id, wine.id))
        
def del_wine_from_wishlist(user:User, wine:Wine):
    with conn:
        c.execute("DELETE FROM wishlist WHERE user_id = ? and wine_id = ?",
                  (user.id, wine.id))
