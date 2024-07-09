import cv2
import face_recognition
import pickle
import os
from database import get_user,get_admin

UPLOADS_DIR = 'E:\\Coding\\Vs Code Studio\\Soft_Final\\uploads'
CAPTURES_DIR = 'E:\\Coding\\Vs Code Studio\\Soft_Final\\captures'
ENCODINGS_FILE = 'E:\\Coding\\Vs Code Studio\\Soft_Final\\encodings.pkl'

# Ensure the directories exist
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(CAPTURES_DIR, exist_ok=True)

# Load existing encodings if available
if os.path.exists(ENCODINGS_FILE):
    try:
        with open(ENCODINGS_FILE, 'rb') as file:
            known_face_encodings = pickle.load(file)
            if not isinstance(known_face_encodings, dict):
                known_face_encodings = {}
    except (pickle.UnpicklingError, EOFError):
        known_face_encodings = {}
else:
    known_face_encodings = {}

def save_encodings():
    with open(ENCODINGS_FILE, 'wb') as file:
        pickle.dump(known_face_encodings, file)

def capture_photo(username):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Press Space to Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            photo_path = os.path.join(CAPTURES_DIR, f'{username}_current.jpg')
            cv2.imwrite(photo_path, frame)
            break
    cap.release()
    cv2.destroyAllWindows()
    return photo_path

def compare_photos(stored_photo_path, current_photo_path):
    stored_image = face_recognition.load_image_file(stored_photo_path)
    current_image = face_recognition.load_image_file(current_photo_path)
    stored_encoding = face_recognition.face_encodings(stored_image)[0]
    current_encoding = face_recognition.face_encodings(current_image)[0]
    results = face_recognition.compare_faces([stored_encoding], current_encoding)
    return results[0]

def recognize_face(username, current_photo_path):
    current_image = face_recognition.load_image_file(current_photo_path)
    current_encoding = face_recognition.face_encodings(current_image)[0]

    if username in known_face_encodings:
        results = face_recognition.compare_faces([known_face_encodings[username]], current_encoding)
        return results[0]
    return False

def perform_key_operation_user(username):
    current_photo_path = capture_photo(username)
    if recognize_face(username, current_photo_path):
        return True
    else:
        user = get_user(username)
        if user:
            stored_photo_path = user['photo_path']
            if compare_photos(stored_photo_path, current_photo_path):
                known_face_encodings[username] = face_recognition.face_encodings(face_recognition.load_image_file(current_photo_path))[0]
                save_encodings()
                return True
    return False

def perform_key_operation_admin(username):
    current_photo_path = capture_photo(username)
    if recognize_face(username, current_photo_path):
        return True
    else:
        user = get_admin(username)
        if user:
            stored_photo_path = user['photo_path']
            if compare_photos(stored_photo_path, current_photo_path):
                known_face_encodings[username] = face_recognition.face_encodings(face_recognition.load_image_file(current_photo_path))[0]
                save_encodings()
                return True
    return False

def add_user_encoding(username, photo_path):
    image = face_recognition.load_image_file(photo_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings[username] = encoding
    save_encodings()
    
def add_admin_encoding(username, photo_path):
    image = face_recognition.load_image_file(photo_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings[username] = encoding
    save_encodings()
