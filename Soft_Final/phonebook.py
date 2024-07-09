import tkinter as tk
import database_user

def show_phonebook(root, username, back_callback):
    for widget in root.winfo_children():
        if not isinstance(widget, tk.Frame):
            widget.destroy()

    tk.Label(root, text="Phone Book", font=("Arial", 24)).pack(pady=20)

    phonebook_form = tk.Frame(root)
    phonebook_form.pack(pady=10)

    tk.Label(phonebook_form, text="Name:", font=("Arial", 12)).pack(anchor='w')
    contact_name = tk.Entry(phonebook_form, font=("Arial", 12), width=30)
    contact_name.pack(anchor='w', pady=2)

    tk.Label(phonebook_form, text="Phone Number:", font=("Arial", 12)).pack(anchor='w')
    phone_number = tk.Entry(phonebook_form, font=("Arial", 12), width=30)
    phone_number.pack(anchor='w', pady=2)

    tk.Button(phonebook_form, text="Add Contact", command=lambda: add_contact_and_reload(root, username, contact_name, phone_number), bg='#2980b9', fg='white').pack(pady=10)
    tk.Button(phonebook_form, text="Back", command=lambda: save_and_back(root, username, back_callback), bg='#34495e', fg='white').pack(pady=10)

    load_contacts(root, username)

def add_contact_and_reload(root, username, name_entry, phone_entry):
    name = name_entry.get()
    phone = phone_entry.get()
    contacts = database_user.load_user_database(username).get("contacts", [])
    contacts.append({"name": name, "phone": phone})
    database_user.save_user_database(username, {"contacts": contacts})
    load_contacts(root, username)

def load_contacts(root, username):
    contacts = database_user.load_user_database(username).get("contacts", [])
    contacts_frame = tk.Frame(root)
    contacts_frame.pack(pady=10, fill='both', expand=True)

    for contact in contacts:
        tk.Label(contacts_frame, text=contact['name'], font=("Arial", 18)).pack(anchor='w')
        tk.Label(contacts_frame, text=contact['phone'], font=("Arial", 12)).pack(anchor='w')

def save_and_back(root, username, back_callback):
    user_data = database_user.load_user_database(username)
    database_user.save_user_database(username, user_data)
    back_callback()
