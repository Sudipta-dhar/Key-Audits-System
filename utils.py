import face_recognition
import os
import pickle

def encode_faces(training_dir='E:/Coding/Vs Code Studio/face_recog_env/data/training'):
    known_encodings = []
    known_names = []

    # Verify the directory path
    if not os.path.exists(training_dir):
        print(f"The directory {training_dir} does not exist.")
        return

    for user_dir in os.listdir(training_dir):
        user_dir_path = os.path.join(training_dir, user_dir)
        if not os.path.isdir(user_dir_path):
            continue
        for img_name in os.listdir(user_dir_path):
            img_path = os.path.join(user_dir_path, img_name)
            try:
                image = face_recognition.load_image_file(img_path)
                encodings = face_recognition.face_encodings(image)

                if len(encodings) > 0:
                    known_encodings.append(encodings[0])
                    known_names.append(user_dir)
            except PermissionError as e:
                print(f"PermissionError: {e} for file {img_path}")
            except Exception as e:
                print(f"Error: {e} for file {img_path}")

    with open('encodings.pkl', 'wb') as f:
        pickle.dump((known_encodings, known_names), f)

    print("Encoding complete")

if __name__ == "__main__":
    encode_faces()
