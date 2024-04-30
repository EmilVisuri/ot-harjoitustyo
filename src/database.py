import sqlite3
import hashlib


def hash_password(password):
    """
    Hashes the given password.

    Args:
    - password (str): The password to be hashed.

    Returns:
    - str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def create_users_table():
    """
    Creates the 'users' table in the database if it does not exist.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT, level INTEGER DEFAULT 1
                    )''')
    conn.commit()
    conn.close()

def add_user(username, password, level):
    """
    Adds a new user to the database.

    Args:
    - username (str): The username of the user.
    - password (str): The password of the user.
    - level (int): The level of the user.

    """
    create_users_table()
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO users (username, password, level) VALUES (?, ?, ?)",
                       (username, hashed_password, level))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Käyttäjätunnus on jo käytössä.")  # Lisätään virheilmoitus

def check_login(username, password):
    """
    Checks if the given username and password match a user in the database.

    Args:
    - username (str): The username of the user.
    - password (str): The password of the user.

    Returns:
    - bool: True if the login is successful, False otherwise.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        hashed_password = hash_password(password)
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                       (username, hashed_password))
        user = cursor.fetchone()
        return user is not None
    finally:
        cursor.close()
        conn.close()

def get_user_level(username):
    """
    Retrieves the level of the given user from the database.

    Args:
    - username (str): The username of the user.

    Returns:
    - int: The level of the user, or None if the user is not found.
    
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT level FROM users WHERE username = ?", (username,))
        level = cursor.fetchone()
        if level:
            return level[0]
        print("Käyttäjän tasoa ei löytynyt.")
        return None
    except sqlite3.Error as e:
        print("Virhe haettaessa käyttäjän tasoa:", e)
        return None
    finally:
        cursor.close()
        conn.close()

def update_level_in_database(username, new_level):
    """
    Updates the level of the given user in the database.

    Args:
    - username (str): The username of the user.
    - new_level (int): The new level to be updated.

    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET level = ? WHERE username = ?", (new_level, username))
        conn.commit()
        print("Käyttäjän taso päivitetty onnistuneesti.")
    except sqlite3.Error as e:
        print("Virhe päivitettäessä käyttäjän tasoa:", e)
    finally:
        cursor.close()
        conn.close()

def get_username():
    """
    Retrieves the username from the database.

    Returns:
    - str: The username, or None if not found.
    
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT username FROM users")
        username = cursor.fetchone()
        if username:
            return username[0]
        print("Käyttäjän käyttäjänimeä ei löytynyt.")
        return None
    except sqlite3.Error as e:
        print("Virhe haettaessa käyttäjän käyttäjänimeä:", e)
        return None
    finally:
        cursor.close()
        conn.close()

def get_level(username):
    """
    Retrieves the level of the given user from the database.

    Args:
    - username (str): The username of the user.

    Returns:
    - int: The level of the user, or None if the user is not found.
    
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT level FROM users WHERE username = ?", (username,))
        level = cursor.fetchone()
        if level:
            return level[0]
        print("Käyttäjän tasoa ei löytynyt.")
        return None
    except sqlite3.Error as e:
        print("Virhe haettaessa käyttäjän tasoa:", e)
        return None
    finally:
        cursor.close()
        conn.close()
