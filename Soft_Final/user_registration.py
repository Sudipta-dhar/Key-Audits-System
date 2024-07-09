import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import auth
import operations

def register_user(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Key Operation Audit")
    root.geometry("800x600")
    photo_path = None

    # Title Frame
    title_frame = tk.Frame(root, bg='green', height=50)
    title_frame.pack(fill='x')
    title_label = tk.Label(title_frame, text="KEY AUDIT SYSTEM", font=("Helvetica", 16), bg='green', fg='white')
    title_label.pack(pady=10)

    # Exit Button
    exit_button = tk.Button(title_frame, text="Exit", command=root.quit, bg='blue', fg='white')
    exit_button.pack(side='right', padx=10)

    # User Registration Label
    user_registration_label = tk.Label(root, text="Users Registrations", font=("Helvetica", 14), bg='white')
    user_registration_label.pack(pady=20)

    # Registration Frame
    registration_frame = tk.Frame(root, bg='white', bd=2, relief='solid')
    registration_frame.pack(pady=20, padx=20)

    # Name Entry
    name_label = tk.Label(registration_frame, text="Name:", font=("Helvetica", 12), bg='white')
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    name_entry = tk.Entry(registration_frame, font=("Helvetica", 12))
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Password Entry
    password_label = tk.Label(registration_frame, text="Password:", font=("Helvetica", 12), bg='white')
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    password_entry = tk.Entry(registration_frame, show='*', font=("Helvetica", 12))
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Upload Picture Label
    upload_picture_label = tk.Label(registration_frame, text="Upload picture", font=("Helvetica", 12), bg='white')
    upload_picture_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    # Picture Frame
    picture_frame = tk.Frame(registration_frame, bg='white', bd=2, relief='solid')
    picture_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Take Picture Button
    def capture_photo():
        nonlocal photo_path
        photo_path = operations.capture_photo(name_entry.get())

    take_picture_button = tk.Button(picture_frame, text="Take picture", command=capture_photo, font=("Helvetica", 12))
    take_picture_button.grid(row=0, column=0, padx=10, pady=10)

    # Choose Picture Button
    def select_photo():
        nonlocal photo_path
        photo_path = filedialog.askopenfilename(title="Select User Photo", initialdir=operations.UPLOADS_DIR, filetypes=[("Image files", "*.jpg *.jpeg *.png")])

    choose_picture_button = tk.Button(picture_frame, text="Choose picture", command=select_photo, font=("Helvetica", 12))
    choose_picture_button.grid(row=0, column=1, padx=10, pady=10)

    # Register Button
    def handle_user_registration():
        username = name_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required.")
            return

        if not photo_path:
            messagebox.showerror("Error", "Photo is required.")
            return

        auth.register_user(username, password, photo_path)
        show_registration_success(username, password, photo_path)

    register_button = tk.Button(root, text="Register", command=handle_user_registration, font=("Helvetica", 12), bg='orange')
    register_button.pack(pady=20)

    # Function to show registration success
    def show_registration_success(username, password, photo_path):
        for widget in root.winfo_children():
            widget.destroy()

        # Title Frame
        title_frame = tk.Frame(root, bg='green', height=50)
        title_frame.pack(fill='x')
        title_label = tk.Label(title_frame, text="KEY AUDIT SYSTEM", font=("Helvetica", 16), bg='green', fg='white')
        title_label.pack(pady=10)

        # Exit Button
        exit_button = tk.Button(title_frame, text="Exit", command=root.quit, bg='blue', fg='white')
        exit_button.pack(side='right', padx=10)

        # Success Frame
        success_frame = tk.Frame(root, bg='white', bd=2, relief='solid')
        success_frame.pack(pady=20, padx=20)

        # Success Message
        success_message = f"Congratulations user ({username}) successful. Your\nUser ID: {username}\nPassword: {password}"
        tk.Label(success_frame, text=success_message, font=("Helvetica", 12), bg='white').pack(pady=20)

        # Picture Label
        image = Image.open(photo_path)
        image = image.resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        picture_label = tk.Label(success_frame, image=photo, bg='gray')
        picture_label.image = photo  # Keep a reference to avoid garbage collection
        picture_label.pack(pady=10, fill='both', expand=True)

        # Back to Menu Button
        back_to_menu_button = tk.Button(root, text="EXIT", command=root.destroy, font=("Helvetica", 12), bg='orange')
        back_to_menu_button.pack(pady=20)

    root.mainloop()
