import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, filedialog
import auth
import admin
import operations
import user_registration  
from user_panel import main, main_menu
import os
from utils import log_operation
import database

PRIMARY_ADMIN_PHOTO = 'E:\\Coding\\Vs Code Studio\\Soft_Final\\primary_admin.jpg'

UPLOADS_DIR = 'E:\\Coding\\Vs Code Studio\\Soft_Final\\uploads'
CAPTURES_DIR = 'E\\Coding\\Vs Code Studio\\Soft_Final\\captures'

class KeyOperationAuditApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Key Operation Audit")
        self.root.geometry("800x650")
        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.root, bg='#4CAF50', height=50)
        header_frame.pack(fill='x')
        tk.Label(header_frame, text="KEY AUDIT SYSTEM", font=("Arial", 24), bg='#4CAF50', fg='white').pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True)

        buttons = [
            ("Primary Administrator", self.primary_admin_login),
            ("Admin Login", self.admin_login),
            ("User Login", self.user_login),
            ("User Registrations", self.user_registration)
        ]

        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command, font=("Arial", 14), width=20, height=2, bg='gray', fg='black').pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 14), bg='#FF5733', fg='white')
        exit_button.pack(pady=20, side='bottom', anchor='e')

##################### Primary Admin Login ########################

    def primary_admin_login(self):
        if not os.path.exists(PRIMARY_ADMIN_PHOTO):
            messagebox.showerror("Error", "Primary admin photo not found.")
            return

        if operations.compare_photos(PRIMARY_ADMIN_PHOTO, operations.capture_photo('primary_admin')):
            self.Primary_admin_panel()
        else:
            messagebox.showerror("Error", "Primary Admin authentication failed")

######################## Admin login ##################

    def admin_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title Frame
        title_frame = tk.Frame(self.root, bg='green', height=50)
        title_frame.pack(fill='x')
        title_label = tk.Label(title_frame, text="KEY AUDIT SYSTEM", font=("Helvetica", 16), bg='green', fg='white')
        title_label.pack(pady=10)

        # Exit Button
        exit_button = tk.Button(title_frame, text="Exit", command=self.root.quit, bg='blue', fg='white')
        exit_button.pack(side='right', padx=10)

        # Admin Login Label
        admin_login_label = tk.Label(self.root, text="Admin login", font=("Helvetica", 14), bg='white')
        admin_login_label.pack(pady=20)

        # Login Frame
        login_frame = tk.Frame(self.root, bg='white', bd=2, relief='solid')
        login_frame.pack(pady=20, padx=20)

        # Name Entry
        name_label = tk.Label(login_frame, text="Name:", font=("Helvetica", 12), bg='white')
        name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.name_entry = tk.Entry(login_frame, font=("Helvetica", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password Entry
        password_label = tk.Label(login_frame, text="Password:", font=("Helvetica", 12), bg='white')
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.password_entry = tk.Entry(login_frame, show='*', font=("Helvetica", 12))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Face Verification Button
        face_verification_button = tk.Button(login_frame, text="Face Verification", command=self.face_verification, font=("Helvetica", 12))
        face_verification_button.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        # Verification Message Box
        self.verification_message = tk.Label(login_frame, text="", font=("Helvetica", 10), bg='white')
        self.verification_message.grid(row=3, column=0, columnspan=2, pady=10)

        # Login Button
        login_button = tk.Button(self.root, text="login", command=self.handle_admin_login, font=("Helvetica", 12), bg='orange')
        login_button.pack(pady=20)

    def face_verification(self):
        face_verified = operations.perform_key_operation_admin(self.name_entry.get())
        if face_verified:
            self.verification_message.config(text="Face verification successful", fg='green')
        else:
            self.verification_message.config(text="Face verification unsuccessful", fg='red')

    def handle_admin_login(self):
        username = self.name_entry.get()
        password = self.password_entry.get()

        if auth.authenticate_admin(username, password):
            if operations.perform_key_operation_admin(username):
                self.admin_panel()
            else:
                messagebox.showerror("Error", "Face authentication failed")
        else:
            messagebox.showerror("Error", "Invalid credentials")

##################### panel Design  ###################

    def Primary_admin_panel(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title Frame
        title_frame = tk.Frame(self.root, bg='green', height=50)
        title_frame.pack(fill='x')
        title_label = tk.Label(title_frame, text="KEY AUDIT SYSTEM", font=("Helvetica", 16), bg='green', fg='white')
        title_label.pack(pady=10)

        # Exit Button
        exit_button = tk.Button(title_frame, text="Exit", command=self.root.quit, bg='blue', fg='white')
        exit_button.pack(side='right', padx=10)

        # Admin Name Label
        admin_name_label = tk.Label(self.root, text="Primary Administrator", font=("Helvetica", 14), bg='gray', fg='black')
        admin_name_label.pack(pady=10)

        # Side Menu Frame
        side_menu_frame = tk.Frame(self.root, bg='white')
        side_menu_frame.pack(side='left', fill='y', padx=20, pady=20)

        # Admin Buttons
        tk.Button(side_menu_frame, text="Add Admin", command=self.add_admin, font=("Helvetica", 12), width=15, bg='gray', fg='black').pack(pady=10)
        tk.Button(side_menu_frame, text="Modify Admin", command=self.modify_admin, font=("Helvetica", 12), width=15, bg='gray', fg='black').pack(pady=10)
        tk.Button(side_menu_frame, text="Delete Admin", command=self.delete_admin, font=("Helvetica", 12), width=15, bg='gray', fg='black').pack(pady=10)
        tk.Button(side_menu_frame, text="List Admins", command=self.list_admin, font=("Helvetica", 12), width=15, bg='gray', fg='black').pack(pady=10)

        # User Buttons
        tk.Button(side_menu_frame, text="Add User", command=self.add_user, font=("Helvetica", 12), width=15, bg='gray', fg='black').pack(pady=10)
        tk.Button(side_menu_frame, text="Modify User", command=self.modify_user, font=("Helvetica", 12), width=15, bg='gray', fg='black').pack(pady=10)
        tk.Button(side_menu_frame, text="Delete User", command=self.delete_user, font=("Helvetica", 12), width=15, bg='gray', fg='black').pack(pady=10)
        tk.Button(side_menu_frame, text="List Users", command=self.list_users, font=("Helvetica", 12), width=15, bg='gray', fg='black').pack(pady=10)

        # Back to Main Menu Button
        back_to_main_button = tk.Button(side_menu_frame, text="Back to Main Menu", command=self.main_menu, font=("Helvetica", 12), width=15, bg='red', fg='white')
        back_to_main_button.pack(pady=10)

        # Main Content Frame
        self.main_content_frame = tk.Frame(self.root, bg='white', bd=2, relief='solid')
        self.main_content_frame.pack(side='right', fill='both', expand=True, padx=20, pady=20)

        # Welcome Label
        welcome_label = tk.Label(self.main_content_frame, text="Welcome", font=("Helvetica", 24), bg='white')
        welcome_label.pack(expand=True)


    def admin_panel(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title Frame
        title_frame = tk.Frame(self.root, bg='green', height=50)
        title_frame.pack(fill='x')
        title_label = tk.Label(title_frame, text="KEY AUDIT SYSTEM", font=("Helvetica", 16), bg='green', fg='white')
        title_label.pack(pady=10)

        # Exit Button
        exit_button = tk.Button(title_frame, text="Exit", command=self.root.quit, bg='blue', fg='white')
        exit_button.pack(side='right', padx=10)

        # Admin Name Label
        admin_name_label = tk.Label(self.root, text="Admin (Name)", font=("Helvetica", 14), bg='gray', fg='black')
        admin_name_label.pack(pady=10)

        # Side Menu Frame
        side_menu_frame = tk.Frame(self.root, bg='white')
        side_menu_frame.pack(side='left', fill='y', padx=20, pady=20)

        # Add User Button
        add_user_button = tk.Button(side_menu_frame, text="Add User", command=self.add_user, font=("Helvetica", 12), width=15, bg='gray', fg='black')
        add_user_button.pack(pady=10)

        # Modify User Button
        modify_user_button = tk.Button(side_menu_frame, text="Modify User", command=self.modify_user, font=("Helvetica", 12), width=15, bg='gray', fg='black')
        modify_user_button.pack(pady=10)

        # Delete User Button
        delete_user_button = tk.Button(side_menu_frame, text="Delete User", command=self.delete_user, font=("Helvetica", 12), width=15, bg='gray', fg='black')
        delete_user_button.pack(pady=10)

        # List Users Button
        list_users_button = tk.Button(side_menu_frame, text="List Users", command=self.list_users, font=("Helvetica", 12), width=15, bg='gray', fg='black')
        list_users_button.pack(pady=10)

        # Main Content Frame
        self.main_content_frame = tk.Frame(self.root, bg='white', bd=2, relief='solid')
        self.main_content_frame.pack(side='right', fill='both', expand=True, padx=20, pady=20)

        # Welcome Label
        welcome_label = tk.Label(self.main_content_frame, text="Welcome", font=("Helvetica", 24), bg='white')
        welcome_label.pack(expand=True)

    ################### Admin Functions ###################
    
    #**************Add Admin ***********************
    def show_add_admin_form(self):
            photo_path = None  # Initialize photo_path here
            # Clear the main content frame
            for widget in self.main_content_frame.winfo_children():
                widget.destroy()

            # Admin Name Label
            admin_name_label = tk.Label(self.main_content_frame, text="Add Admin", font=("Helvetica", 14), bg='gray', fg='black')
            admin_name_label.pack(pady=10)

            # Entry fields for User details
            tk.Label(self.main_content_frame, text="Name:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
            name_entry = tk.Entry(self.main_content_frame, font=("Helvetica", 12))
            name_entry.pack(pady=5, padx=10, fill='x')

            tk.Label(self.main_content_frame, text="Password:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
            password_entry = tk.Entry(self.main_content_frame, show='*', font=("Helvetica", 12))
            password_entry.pack(pady=5, padx=10, fill='x')

            tk.Label(self.main_content_frame, text="Upload picture", font=("Helvetica", 12), bg='white').pack(pady=10)

            picture_frame = tk.Frame(self.main_content_frame, bg='white', bd=2, relief='solid')
            picture_frame.pack(pady=10)

            def capture_photo():
                nonlocal photo_path
                photo_path = operations.capture_photo(name_entry.get())

            def select_photo():
                nonlocal photo_path
                photo_path = filedialog.askopenfilename(title="Select User Photo", initialdir=UPLOADS_DIR, filetypes=[("Image files", "*.jpg *.jpeg *.png")])

            take_picture_button = tk.Button(picture_frame, text="Take picture", command=capture_photo, font=("Helvetica", 12), bg='gray')
            take_picture_button.grid(row=0, column=0, padx=10, pady=10)

            choose_picture_button = tk.Button(picture_frame, text="Choose picture", command=select_photo, font=("Helvetica", 12), bg='gray')
            choose_picture_button.grid(row=0, column=1, padx=10, pady=10)

            def save_admin():
                username = name_entry.get()
                password = password_entry.get()

                if username and password and photo_path:
                    auth.register_admin(username, password, photo_path)
                    messagebox.showinfo("Success", f"Admin {username} added successfully.")
                    self.Primary_admin_panel()
                else:
                    messagebox.showerror("Error", "All fields are required.")

            save_button = tk.Button(self.main_content_frame, text="Save", command=save_admin, font=("Helvetica", 12), bg='orange')
            save_button.pack(pady=10)
            
    def add_admin(self):
        self.show_add_admin_form()
        
    #**************Delete Admin ***********************
    def show_delete_admin_form(self):
        # Clear the main content frame
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        # Admin Name Label
        admin_name_label = tk.Label(self.main_content_frame, text="Delete Admin", font=("Helvetica", 14), bg='gray', fg='black')
        admin_name_label.pack(pady=10)

        # Entry field for Admin name to delete
        tk.Label(self.main_content_frame, text="Name:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
        name_entry = tk.Entry(self.main_content_frame, font=("Helvetica", 12))
        name_entry.pack(pady=5, padx=10, fill='x')

        # List of admins
        admin_list_frame = tk.Frame(self.main_content_frame, bg='white', bd=2, relief='solid')
        admin_list_frame.pack(pady=10)

        tk.Label(admin_list_frame, text="Admin List", font=("Helvetica", 12), bg='white').grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        admins = database.list_admin()  # Fetch the list of admins

        tk.Label(admin_list_frame, text="Name", font=("Helvetica", 12), bg='white').grid(row=1, column=0, padx=10, pady=5)
        tk.Label(admin_list_frame, text="Password", font=("Helvetica", 12), bg='white').grid(row=1, column=1, padx=10, pady=5)
        tk.Label(admin_list_frame, text="Picture", font=("Helvetica", 12), bg='white').grid(row=1, column=2, padx=10, pady=5)

        for i, admin in enumerate(admins, start=2):
            tk.Label(admin_list_frame, text=admin, font=("Helvetica", 12), bg='white').grid(row=i, column=0, padx=10, pady=5)
            tk.Label(admin_list_frame, text="********", font=("Helvetica", 12), bg='white').grid(row=i, column=1, padx=10, pady=5)
            tk.Label(admin_list_frame, text=database.get_admin(admin)['photo_path'], font=("Helvetica", 12), bg='white').grid(row=i, column=2, padx=10, pady=5)

        def delete_admin():
            username = name_entry.get()
            if username:
                database.delete_admin(username)
                messagebox.showinfo("Success", f"Admin {username} deleted successfully.")
                self.Primary_admin_panel()
            else:
                messagebox.showerror("Error", "Username is required.")

        delete_button = tk.Button(self.main_content_frame, text="Delete", command=delete_admin, font=("Helvetica", 12), bg='orange')
        delete_button.pack(pady=10)
            
    def delete_admin(self):
        self.show_delete_admin_form()
        
    #**************Modify Admin ***********************
    def show_modify_admin_form(self):
        # Clear the main content frame
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        # Admin Name Label
        admin_name_label = tk.Label(self.main_content_frame, text="Modify Admin", font=("Helvetica", 14), bg='gray', fg='black')
        admin_name_label.pack(pady=10)

        # Entry fields for Admin details
        tk.Label(self.main_content_frame, text="Name:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
        name_entry = tk.Entry(self.main_content_frame, font=("Helvetica", 12))
        name_entry.pack(pady=5, padx=10, fill='x')

        tk.Label(self.main_content_frame, text="Password:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
        password_entry = tk.Entry(self.main_content_frame, show='*', font=("Helvetica", 12))
        password_entry.pack(pady=5, padx=10, fill='x')

        tk.Label(self.main_content_frame, text="Upload picture", font=("Helvetica", 12), bg='white').pack(pady=10)

        picture_frame = tk.Frame(self.main_content_frame, bg='white', bd=2, relief='solid')
        picture_frame.pack(pady=10)

        photo_path = None  # Initialize photo_path here

        def capture_photo():
            nonlocal photo_path
            photo_path = operations.capture_photo(name_entry.get())

        def select_photo():
            nonlocal photo_path
            photo_path = filedialog.askopenfilename(title="Select Admin Photo", initialdir=UPLOADS_DIR, filetypes=[("Image files", "*.jpg *.jpeg *.png")])

        take_picture_button = tk.Button(picture_frame, text="Take picture", command=capture_photo, font=("Helvetica", 12), bg='gray')
        take_picture_button.grid(row=0, column=0, padx=10, pady=10)

        choose_picture_button = tk.Button(picture_frame, text="Choose picture", command=select_photo, font=("Helvetica", 12), bg='gray')
        choose_picture_button.grid(row=0, column=1, padx=10, pady=10)

        # List of admins
        admin_list_frame = tk.Frame(self.main_content_frame, bg='white', bd=2, relief='solid')
        admin_list_frame.pack(pady=10)

        tk.Label(admin_list_frame, text="Admin List", font=("Helvetica", 12), bg='white').grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        admins = database.list_admin()  # Fetch the list of admins

        tk.Label(admin_list_frame, text="Name", font=("Helvetica", 12), bg='white').grid(row=1, column=0, padx=10, pady=5)
        tk.Label(admin_list_frame, text="Password", font=("Helvetica", 12), bg='white').grid(row=1, column=1, padx=10, pady=5)
        tk.Label(admin_list_frame, text="Picture", font=("Helvetica", 12), bg='white').grid(row=1, column=2, padx=10, pady=5)

        for i, admin in enumerate(admins, start=2):
            tk.Label(admin_list_frame, text=admin, font=("Helvetica", 12), bg='white').grid(row=i, column=0, padx=10, pady=5)
            tk.Label(admin_list_frame, text="********", font=("Helvetica", 12), bg='white').grid(row=i, column=1, padx=10, pady=5)
            tk.Label(admin_list_frame, text=database.get_admin(admin)['photo_path'], font=("Helvetica", 12), bg='white').grid(row=i, column=2, padx=10, pady=5)

        def modify_admin():
            username = name_entry.get()
            password = password_entry.get()

            if username:
                new_data = {}
                if password:
                    new_data['password'] = auth.hash_password(password)
                if photo_path:
                    new_data['photo_path'] = photo_path
                database.modify_admin(username, new_data)
                messagebox.showinfo("Success", f"Admin {username} modified successfully.")
                self.Primary_admin_panel()
            else:
                messagebox.showerror("Error", "Username is required.")
                
        modify_button = tk.Button(self.main_content_frame, text="Modify", command=modify_admin, font=("Helvetica", 12), bg='orange')
        modify_button.pack(pady=10)
        
    def modify_admin(self):
        self.show_modify_admin_form()
        
    #**************List Admin ***********************
    def list_admin(self):
        admins = database.load_database(database.ADMIN_DATABASE_FILE)  # Fetch from database
        admin_data = [(username, '*' * len(data['password']), data['photo_path']) for username, data in admins.items()]
        self.display_admin_list(admin_data)

    def display_admin_list(self, admins):
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        columns = ('Name', 'Password', 'Picture')
        tree = ttk.Treeview(self.main_content_frame, columns=columns, show='headings')
        tree.heading('Name', text='Name')
        tree.heading('Password', text='Password')
        tree.heading('Picture', text='Picture')

        # Set column widths
        tree.column('Name', width=200, anchor=tk.W)
        tree.column('Password', width=200, anchor=tk.W)
        tree.column('Picture', width=200, anchor=tk.W)

        for admin in admins:
            tree.insert('', tk.END, values=admin)

        scrollbar = ttk.Scrollbar(self.main_content_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill='both', expand=True)
        
################### User Functions ###################
    
    #**************Add user***********************
    def show_add_user_form(self):
        photo_path = None  # Initialize photo_path here
        # Clear the main content frame
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        # Admin Name Label
        admin_name_label = tk.Label(self.main_content_frame, text="Add User", font=("Helvetica", 14), bg='gray', fg='black')
        admin_name_label.pack(pady=10)

        # Entry fields for User details
        tk.Label(self.main_content_frame, text="Name:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
        name_entry = tk.Entry(self.main_content_frame, font=("Helvetica", 12))
        name_entry.pack(pady=5, padx=10, fill='x')

        tk.Label(self.main_content_frame, text="Password:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
        password_entry = tk.Entry(self.main_content_frame, show='*', font=("Helvetica", 12))
        password_entry.pack(pady=5, padx=10, fill='x')

        tk.Label(self.main_content_frame, text="Upload picture", font=("Helvetica", 12), bg='white').pack(pady=10)

        picture_frame = tk.Frame(self.main_content_frame, bg='white', bd=2, relief='solid')
        picture_frame.pack(pady=10)

        def capture_photo():
            nonlocal photo_path
            photo_path = operations.capture_photo(name_entry.get())

        def select_photo():
            nonlocal photo_path
            photo_path = filedialog.askopenfilename(title="Select User Photo", initialdir=UPLOADS_DIR, filetypes=[("Image files", "*.jpg *.jpeg *.png")])

        take_picture_button = tk.Button(picture_frame, text="Take picture", command=capture_photo, font=("Helvetica", 12), bg='gray')
        take_picture_button.grid(row=0, column=0, padx=10, pady=10)

        choose_picture_button = tk.Button(picture_frame, text="Choose picture", command=select_photo, font=("Helvetica", 12), bg='gray')
        choose_picture_button.grid(row=0, column=1, padx=10, pady=10)

        def save_user():
            username = name_entry.get()
            password = password_entry.get()

            if username and password and photo_path:
                auth.register_user(username, password, photo_path)
                messagebox.showinfo("Success", f"User {username} added successfully.")
                self.Primary_admin_panel()
            else:
                messagebox.showerror("Error", "All fields are required.")

        save_button = tk.Button(self.main_content_frame, text="Save", command=save_user, font=("Helvetica", 12), bg='orange')
        save_button.pack(pady=10)

    def add_user(self):
        self.show_add_user_form()
        
    #**************Delete User ***********************
    def show_delete_user_form(self):
        # Clear the main content frame
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        # Admin Name Label
        admin_name_label = tk.Label(self.main_content_frame, text="Delete User", font=("Helvetica", 14), bg='gray', fg='black')
        admin_name_label.pack(pady=10)

        # Entry field for User name to delete
        tk.Label(self.main_content_frame, text="Name:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
        name_entry = tk.Entry(self.main_content_frame, font=("Helvetica", 12))
        name_entry.pack(pady=5, padx=10, fill='x')

        # List of users
        user_list_frame = tk.Frame(self.main_content_frame, bg='white', bd=2, relief='solid')
        user_list_frame.pack(pady=10)

        tk.Label(user_list_frame, text="User List", font=("Helvetica", 12), bg='white').grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        users = database.list_users()  # Fetch the list of users

        tk.Label(user_list_frame, text="Name", font=("Helvetica", 12), bg='white').grid(row=1, column=0, padx=10, pady=5)
        tk.Label(user_list_frame, text="Password", font=("Helvetica", 12), bg='white').grid(row=1, column=1, padx=10, pady=5)
        tk.Label(user_list_frame, text="Picture", font=("Helvetica", 12), bg='white').grid(row=1, column=2, padx=10, pady=5)

        for i, user in enumerate(users, start=2):
            tk.Label(user_list_frame, text=user, font=("Helvetica", 12), bg='white').grid(row=i, column=0, padx=10, pady=5)
            tk.Label(user_list_frame, text="********", font=("Helvetica", 12), bg='white').grid(row=i, column=1, padx=10, pady=5)
            tk.Label(user_list_frame, text=database.get_user(user)['photo_path'], font=("Helvetica", 12), bg='white').grid(row=i, column=2, padx=10, pady=5)

        def delete_user():
            username = name_entry.get()
            if username:
                database.delete_user(username)
                messagebox.showinfo("Success", f"User {username} deleted successfully.")
                self.Primary_admin_panel()
            else:
                messagebox.showerror("Error", "Username is required.")

        delete_button = tk.Button(self.main_content_frame, text="Delete", command=delete_user, font=("Helvetica", 12), bg='orange')
        delete_button.pack(pady=10)

            
    def delete_user(self):
        self.show_delete_user_form()     
              
    #**************Modefy User ***********************
    def show_modify_user_form(self):
        # Clear the main content frame
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        # Admin Name Label
        admin_name_label = tk.Label(self.main_content_frame, text="Modify User", font=("Helvetica", 14), bg='gray', fg='black')
        admin_name_label.pack(pady=10)

        # Entry fields for User details
        tk.Label(self.main_content_frame, text="Name:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
        name_entry = tk.Entry(self.main_content_frame, font=("Helvetica", 12))
        name_entry.pack(pady=5, padx=10, fill='x')

        tk.Label(self.main_content_frame, text="Password:", font=("Helvetica", 12), bg='white').pack(pady=5, anchor='w', padx=10)
        password_entry = tk.Entry(self.main_content_frame, show='*', font=("Helvetica", 12))
        password_entry.pack(pady=5, padx=10, fill='x')

        tk.Label(self.main_content_frame, text="Upload picture", font=("Helvetica", 12), bg='white').pack(pady=10)

        picture_frame = tk.Frame(self.main_content_frame, bg='white', bd=2, relief='solid')
        picture_frame.pack(pady=10)

        photo_path = None  # Initialize photo_path here

        def capture_photo():
            nonlocal photo_path
            photo_path = operations.capture_photo(name_entry.get())

        def select_photo():
            nonlocal photo_path
            photo_path = filedialog.askopenfilename(title="Select User Photo", initialdir=UPLOADS_DIR, filetypes=[("Image files", "*.jpg *.jpeg *.png")])

        take_picture_button = tk.Button(picture_frame, text="Take picture", command=capture_photo, font=("Helvetica", 12), bg='gray')
        take_picture_button.grid(row=0, column=0, padx=10, pady=10)

        choose_picture_button = tk.Button(picture_frame, text="Choose picture", command=select_photo, font=("Helvetica", 12), bg='gray')
        choose_picture_button.grid(row=0, column=1, padx=10, pady=10)

        # List of users
        user_list_frame = tk.Frame(self.main_content_frame, bg='white', bd=2, relief='solid')
        user_list_frame.pack(pady=10)

        tk.Label(user_list_frame, text="User List", font=("Helvetica", 12), bg='white').grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        users = database.list_users()  # Fetch the list of users

        tk.Label(user_list_frame, text="Name", font=("Helvetica", 12), bg='white').grid(row=1, column=0, padx=10, pady=5)
        tk.Label(user_list_frame, text="Password", font=("Helvetica", 12), bg='white').grid(row=1, column=1, padx=10, pady=5)
        tk.Label(user_list_frame, text="Picture", font=("Helvetica", 12), bg='white').grid(row=1, column=2, padx=10, pady=5)

        for i, user in enumerate(users, start=2):
            tk.Label(user_list_frame, text=user, font=("Helvetica", 12), bg='white').grid(row=i, column=0, padx=10, pady=5)
            tk.Label(user_list_frame, text="********", font=("Helvetica", 12), bg='white').grid(row=i, column=1, padx=10, pady=5)
            tk.Label(user_list_frame, text=database.get_user(user)['photo_path'], font=("Helvetica", 12), bg='white').grid(row=i, column=2, padx=10, pady=5)

        def modify_user():
            username = name_entry.get()
            password = password_entry.get()

            if username:
                new_data = {}
                if password:
                    new_data['password'] = auth.hash_password(password)
                if photo_path:
                    new_data['photo_path'] = photo_path
                database.modify_user(username, new_data)
                messagebox.showinfo("Success", f"User {username} modified successfully.")
                self.Primary_admin_panel()
            else:
                messagebox.showerror("Error", "Username is required.")

        modify_button = tk.Button(self.main_content_frame, text="Modify", command=modify_user, font=("Helvetica", 12), bg='orange')
        modify_button.pack(pady=10)
        
    def modify_user(self):
        self.show_modify_user_form()
            
    #**************Modefy User ***********************
    def list_users(self):
        users = database.load_database(database.USER_DATABASE_FILE)  # Fetch from database
        user_data = [(username, '*' * len(data['password']), data['photo_path']) for username, data in users.items()]
        self.display_user_list(user_data)
        
        
    def display_user_list(self, users):
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        columns = ('Name', 'Password', 'Picture')
        tree = ttk.Treeview(self.main_content_frame, columns=columns, show='headings')
        tree.heading('Name', text='Name')
        tree.heading('Password', text='Password')
        tree.heading('Picture', text='Picture')

        # Set column widths
        tree.column('Name', width=200, anchor=tk.W)
        tree.column('Password', width=200, anchor=tk.W)
        tree.column('Picture', width=200, anchor=tk.W)

        for user in users:
            tree.insert('', tk.END, values=user)

        scrollbar = ttk.Scrollbar(self.main_content_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill='both', expand=True)

###################### User Login ####################

    def user_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title Frame
        title_frame = tk.Frame(self.root, bg='green', height=50)
        title_frame.pack(fill='x')
        title_label = tk.Label(title_frame, text="KEY AUDIT SYSTEM", font=("Helvetica", 16), bg='green', fg='white')
        title_label.pack(pady=10)

        # Exit Button
        exit_button = tk.Button(title_frame, text="Exit", command=self.root.quit, bg='blue', fg='white')
        exit_button.pack(side='right', padx=10)

        # User Login Label
        user_login_label = tk.Label(self.root, text="User login", font=("Helvetica", 14), bg='white')
        user_login_label.pack(pady=20)

        # Login Frame
        login_frame = tk.Frame(self.root, bg='white', bd=2, relief='solid')
        login_frame.pack(pady=20, padx=20)

        # Name Entry
        name_label = tk.Label(login_frame, text="Name:", font=("Helvetica", 12), bg='white')
        name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.name_entry = tk.Entry(login_frame, font=("Helvetica", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password Entry
        password_label = tk.Label(login_frame, text="Password:", font=("Helvetica", 12), bg='white')
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.password_entry = tk.Entry(login_frame, show='*', font=("Helvetica", 12))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Face Verification Button
        face_verification_button = tk.Button(login_frame, text="Face Verification", command=self.face_verification_user, font=("Helvetica", 12))
        face_verification_button.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        # Verification Message Box
        self.verification_message = tk.Label(login_frame, text="", font=("Helvetica", 10), bg='white')
        self.verification_message.grid(row=3, column=0, columnspan=2, pady=10)

        # Login Button
        login_button = tk.Button(self.root, text="login", command=self.handle_user_login, font=("Helvetica", 12), bg='orange')
        login_button.pack(pady=20)
        
    def face_verification_user(self):
        face_verified = operations.perform_key_operation_user(self.name_entry.get())
        if face_verified:
            self.verification_message.config(text="Face verification successful", fg='green')
        else:
            self.verification_message.config(text="Face verification unsuccessful", fg='red')
            
    def handle_user_login(self):
        username = self.name_entry.get()
        password = self.password_entry.get()

        if auth.authenticate_user(username, password):
            if operations.perform_key_operation_user(username):
                messagebox.showinfo("Success", "Login successful.")
                self.root.destroy()
                main(username)
            else:
                messagebox.showerror("Error", "Face authentication failed.")
        else:
            messagebox.showerror("Error", "Invalid credentials.")
  
###################### User-Registeration Login ####################
        
    def user_registration(self):
        user_registration.register_user(self.root)  # Call the user registration function
        



if __name__ == '__main__':
    root = tk.Tk()
    app = KeyOperationAuditApp(root)
    root.mainloop()
