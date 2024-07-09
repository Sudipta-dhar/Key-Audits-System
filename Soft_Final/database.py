import os
import json

# Define the database directory path
DATABASE_DIR = 'E:\\Coding\\Vs Code Studio\\Soft_Final\\DataBase'

# Define file paths for user and admin databases
USER_DATABASE_FILE = os.path.join(DATABASE_DIR, 'user_db.json')
ADMIN_DATABASE_FILE = os.path.join(DATABASE_DIR, 'admin_db.json')

# Ensure the directory exists
os.makedirs(DATABASE_DIR, exist_ok=True)

def load_database(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_database(database, file_path):
    with open(file_path, 'w') as file:
        json.dump(database, file, indent=4)

#### Admin DataBase Functions

def get_admin(username):
    database = load_database(ADMIN_DATABASE_FILE)
    return database.get(username)

def add_admin(username, user_data):
    database = load_database(ADMIN_DATABASE_FILE)
    database[username] = user_data
    save_database(database, ADMIN_DATABASE_FILE)

def delete_admin(username):
    database = load_database(ADMIN_DATABASE_FILE)
    if username in database:
        del database[username]
        save_database(database, ADMIN_DATABASE_FILE)

def modify_admin(username, new_data):
    database = load_database(ADMIN_DATABASE_FILE)
    if username in database:
        database[username].update(new_data)
        save_database(database, ADMIN_DATABASE_FILE)

def list_admin():
    database = load_database(ADMIN_DATABASE_FILE)
    return list(database.keys())

#### User DataBase Functions

def get_user(username):
    database = load_database(USER_DATABASE_FILE)
    return database.get(username)

def add_user(username, user_data):
    database = load_database(USER_DATABASE_FILE)
    database[username] = user_data
    save_database(database, USER_DATABASE_FILE)

def delete_user(username):
    database = load_database(USER_DATABASE_FILE)
    if username in database:
        del database[username]
        save_database(database, USER_DATABASE_FILE)

def modify_user(username, new_data):
    database = load_database(USER_DATABASE_FILE)
    if username in database:
        database[username].update(new_data)
        save_database(database, USER_DATABASE_FILE)

def list_users():
    database = load_database(USER_DATABASE_FILE)
    return list(database.keys())
