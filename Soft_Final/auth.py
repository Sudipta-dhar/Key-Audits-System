import bcrypt
from database import add_user, get_user, get_admin, add_admin
import operations

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def register_user(username, password, photo_path):
    hashed_password = hash_password(password)
    user_data = {
        'password': hashed_password,
        'photo_path': photo_path
    }
    add_user(username, user_data)
    operations.add_user_encoding(username, photo_path)

def register_admin(username, password, photo_path):
    hashed_password = hash_password(password)
    admin_data = {
        'password': hashed_password,
        'photo_path': photo_path
    }
    add_admin(username, admin_data)
    operations.add_user_encoding(username, photo_path)

def authenticate_user(username, password):
    user = get_user(username)
    if user and check_password(password, user['password']):
        return True
    return False

def authenticate_admin(username, password):
    admin = get_admin(username)
    if admin and check_password(password, admin['password']):
        return True
    return False
