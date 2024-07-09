import tkinter as tk
import time
import database_user

def show_notebook(root, username, back_callback):
    for widget in root.winfo_children():
        if not isinstance(widget, tk.Frame):
            widget.destroy()

    tk.Label(root, text="Notebook", font=("Arial", 24)).pack(pady=20)

    note_form = tk.Frame(root)
    note_form.pack(pady=10)

    tk.Label(note_form, text="Title:", font=("Arial", 12)).pack(anchor='w')
    note_title = tk.Entry(note_form, font=("Arial", 12), width=30)
    note_title.pack(anchor='w', pady=2)

    tk.Label(note_form, text="Body:", font=("Arial", 12)).pack(anchor='w')
    note_body = tk.Text(note_form, font=("Arial", 12), width=30, height=10)
    note_body.pack(anchor='w', pady=2)

    tk.Button(note_form, text="Add Note", command=lambda: add_note_and_reload(root, username, note_title, note_body), bg='#2980b9', fg='white').pack(pady=10)
    tk.Button(note_form, text="Back", command=lambda: save_and_back(root, username, back_callback), bg='#34495e', fg='white').pack(pady=10)

    load_notes(root, username)

def add_note_and_reload(root, username, title_entry, body_text):
    title = title_entry.get()
    body = body_text.get("1.0", tk.END)
    notes = database_user.load_user_database(username).get("notes", [])
    notes.append({"title": title, "body": body, "date": time.strftime("%Y-%m-%d %H:%M:%S")})
    database_user.save_user_database(username, {"notes": notes})
    load_notes(root, username)

def load_notes(root, username):
    notes = database_user.load_user_database(username).get("notes", [])
    notes_frame = tk.Frame(root)
    notes_frame.pack(pady=10, fill='both', expand=True)

    for note in notes:
        tk.Label(notes_frame, text=note['title'], font=("Arial", 18)).pack(anchor='w')
        tk.Label(notes_frame, text=note['body'], font=("Arial", 12)).pack(anchor='w')
        tk.Label(notes_frame, text=note['date'], font=("Arial", 8)).pack(anchor='w')

def save_and_back(root, username, back_callback):
    user_data = database_user.load_user_database(username)
    database_user.save_user_database(username, user_data)
    back_callback()
