import os
import json

BASE_DIR = 'E:\\Coding\\Vs Code Studio\\Soft_Final\\DataBase\\userdatabase'

def get_user_db_path(username):
    os.makedirs(BASE_DIR, exist_ok=True)
    return os.path.join(BASE_DIR, f"{username}_data.json")

def load_user_database(username):
    db_path = get_user_db_path(username)
    if os.path.exists(db_path):
        with open(db_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_user_database(username, data):
    db_path = get_user_db_path(username)
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    with open(db_path, 'w') as file:
        json.dump(data, file, indent=4)
