import tkinter as tk
from tkinter import messagebox
import about
import notebook
import phonebook
import database_user

class UserPanel:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.create_sidebar()
        self.show_welcome()

    def create_sidebar(self):
        self.sidebar = tk.Frame(self.root, bg='#2c3e50', width=200, height=500)
        self.sidebar.pack(expand=False, fill='y', side='left', anchor='nw')

        self.buttons = {
            "About": self.show_about,
            "Notebook": self.show_notebook,
            "Phone Book": self.show_phonebook,
            "Logout": self.logout
        }

        for button_text, command in self.buttons.items():
            tk.Button(self.sidebar, text=button_text, command=command, width=20, bg='#34495e', fg='white').pack(pady=10)

    def show_welcome(self):
        self.clear_frame()
        tk.Label(self.root, text=f"Welcome, {self.username}!", font=("Arial", 24)).pack(pady=20)

    def show_about(self):
        self.clear_frame()
        about.show_about(self.root, self.username, self.show_welcome)

    def show_notebook(self):
        self.clear_frame()
        notebook.show_notebook(self.root, self.username, self.show_welcome)

    def show_phonebook(self):
        self.clear_frame()
        phonebook.show_phonebook(self.root, self.username, self.show_welcome)

    def logout(self):
        self.save_all_data()
        self.root.destroy()
        main_menu()

    def save_all_data(self):
        # Placeholder for saving any pending data if necessary
        user_data = database_user.load_user_database(self.username)
        database_user.save_user_database(self.username, user_data)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            if widget != self.sidebar:
                widget.destroy()

def main(username):
    root = tk.Tk()
    root.geometry("800x600")
    app = UserPanel(root, username)
    root.mainloop()

def main_menu():
    root = tk.Tk()
    app = app(root)
    root.mainloop()
