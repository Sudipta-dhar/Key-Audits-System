from database import add_user, delete_user, modify_user, list_users, get_user
from auth import hash_password

def admin_add_user(username, password, photo_path):
    hashed_password = hash_password(password)
    user_data = {
        'password': hashed_password,
        'photo_path': photo_path
    }
    add_user(username, user_data)

def admin_delete_user(username):
    delete_user(username)

def admin_modify_user(username, new_password=None, new_photo_path=None):
    new_data = {}
    if new_password:
        new_data['password'] = hash_password(new_password)
    if new_photo_path:
        new_data['photo_path'] = new_photo_path
    modify_user(username, new_data)

def admin_list_users():
    return list_users()
