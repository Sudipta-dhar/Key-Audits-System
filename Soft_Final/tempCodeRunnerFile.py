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