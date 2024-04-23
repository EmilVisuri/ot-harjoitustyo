import sqlite3
import hashlib


def Hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def Create_users_table():
    Conn = sqlite3.connect('users.db')
    Cursor = Conn.cursor()
    Cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT, level INTEGER DEFAULT 1
                    )''')
    Conn.commit()
    Conn.close()

def Add_user(username, password, level):
    Create_users_table()
    Conn = sqlite3.connect('users.db')
    Cursor = Conn.cursor()
    try:
        Hashed_password = Hash_password(password)
        Cursor.execute("INSERT INTO users (username, password, level) VALUES (?, ?, ?)", (username, Hashed_password, level))
        Conn.commit()
    except sqlite3.IntegrityError:
        print("Käyttäjätunnus on jo käytössä.")

def Check_login(username, password):
    Conn = sqlite3.connect('users.db')
    Cursor = Conn.cursor()
    try:
        Hashed_password = Hash_password(password)
        Cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, Hashed_password))
        user = Cursor.fetchone()
        return user is not None
    finally:
        Cursor.close()
        Conn.close()
        
        
def Get_user_level(username):
    Conn = sqlite3.connect('users.db')
    Cursor = Conn.cursor()
    try:
        Cursor.execute("SELECT level FROM users WHERE username = ?", (username,))
        level = Cursor.fetchone()
        if level:
            return level[0]
        else:
            print("Käyttäjän tasoa ei löytynyt.")
            return None
    except sqlite3.Error as e:
        print("Virhe haettaessa käyttäjän tasoa:", e)
        return None
    finally:
        Cursor.close()
        Conn.close()        
        
def Update_level_in_database(username, new_level):
    Conn = sqlite3.connect('users.db')
    Cursor = Conn.cursor()
    try:
        Cursor.execute("UPDATE users SET level = ? WHERE username = ?", (new_level, username))
        Conn.commit()
        print("Käyttäjän taso päivitetty onnistuneesti.")
    except sqlite3.Error as e:
        print("Virhe päivitettäessä käyttäjän tasoa:", e)
    finally:
        Cursor.close()
        Conn.close()
        
def Get_username():
    Conn = sqlite3.connect('users.db')
    Cursor = Conn.cursor()
    try:
        Cursor.execute("SELECT username FROM users")
        username = Cursor.fetchone()
        if username:
            return username[0]
        else:
            print("Käyttäjän käyttäjänimeä ei löytynyt.")
            return None
    except sqlite3.Error as e:
        print("Virhe haettaessa käyttäjän käyttäjänimeä:", e)
        return None
    finally:
        Cursor.close()
        Conn.close()

def Get_level(username):
    Conn = sqlite3.connect('users.db')
    Cursor = Conn.cursor()
    try:
        Cursor.execute("SELECT level FROM users WHERE username = ?", (username,))
        level = Cursor.fetchone()
        if level:
            return level[0]
        else:
            print("Käyttäjän tasoa ei löytynyt.")
            return None
    except sqlite3.Error as e:
        print("Virhe haettaessa käyttäjän tasoa:", e)
        return None
    finally:
        Cursor.close()
        Conn.close()
        