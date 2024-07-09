import tkinter as tk
from tkinter import messagebox
import database_user

def show_about(root, username, back_callback):
    for widget in root.winfo_children():
        if not isinstance(widget, tk.Frame):
            widget.destroy()

    tk.Label(root, text="About", font=("Arial", 24)).pack(pady=20)

    user_data = database_user.load_user_database(username)

    about_frame = tk.Frame(root)
    about_frame.pack(pady=10, fill='both', expand=True)

    personal_info_frame = tk.Frame(about_frame)
    personal_info_frame.pack(side='left', fill='both', expand=True, padx=10)

    travel_info_frame = tk.Frame(about_frame)
    travel_info_frame.pack(side='right', fill='both', expand=True, padx=10)

    fields = {
        "personal_info": ['Gender', 'Age', 'Birthdate', 'Address', 'Country', 'Phone Number', 'Email Id', 'Email Password'],
        "travel_info": ['National ID', 'Passport Id', 'Driving license', 'Current Visa', 'Visa Number', 'Current number']
    }

    entries = {}

    for field in fields["personal_info"]:
        tk.Label(personal_info_frame, text=f"{field}:", font=("Arial", 12)).pack(anchor='w')
        value = user_data.get(field.lower().replace(' ', '_'), 'None')
        entry = tk.Entry(personal_info_frame, font=("Arial", 12), width=30)
        entry.insert(0, value)
        entry.pack(anchor='w', pady=2)
        entries[field.lower().replace(' ', '_')] = entry

    for field in fields["travel_info"]:
        tk.Label(travel_info_frame, text=f"{field}:", font=("Arial", 12)).pack(anchor='w')
        value = user_data.get(field.lower().replace(' ', '_'), 'None')
        entry = tk.Entry(travel_info_frame, font=("Arial", 12), width=30)
        entry.insert(0, value)
        entry.pack(anchor='w', pady=2)
        entries[field.lower().replace(' ', '_')] = entry

    tk.Button(root, text="Save", command=lambda: save_about(username, entries), bg='#2980b9', fg='white').pack(pady=10)
    tk.Button(root, text="Back", command=lambda: save_and_back(username, entries, back_callback), bg='#34495e', fg='white').pack(pady=10)

def save_about(username, entries):
    data = {field: entry.get() for field, entry in entries.items()}
    database_user.save_user_database(username, data)
    messagebox.showinfo("Success", "User information saved.")

def save_and_back(username, entries, back_callback):
    save_about(username, entries)
    back_callback()
