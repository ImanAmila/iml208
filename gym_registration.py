import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AuthenticationSystem:
    def __init__(self, root, registration_system):
        self.root = root
        self.root.title("Authentication System")
        self.root.configure(bg='#ffd700')  # Set background color to yellow

        self.registration_system = registration_system

        self.users = {"user1": "password1", "user2": "password2"}  # Replace with your own user credentials

        self.create_widgets()

    def create_widgets(self):
        self.username_label = ttk.Label(self.root, text="Username:", background='#ffd700')  # Set background color
        self.username_entry = ttk.Entry(self.root)

        self.password_label = ttk.Label(self.root, text="Password:", background='#ffd700')  # Set background color
        self.password_entry = ttk.Entry(self.root, show="*")

        self.login_button = ttk.Button(self.root, text="Log In", command=self.log_in, style='TButton')  # Apply a style for the button
        self.signup_button = ttk.Button(self.root, text="Sign Up", command=self.sign_up, style='TButton')  # Apply a style for the button

        self.username_label.grid(row=0, column=0, pady=10, sticky=tk.E)
        self.username_entry.grid(row=0, column=1, pady=10)

        self.password_label.grid(row=1, column=0, pady=10, sticky=tk.E)
        self.password_entry.grid(row=1, column=1, pady=10)

        self.login_button.grid(row=2, column=0, columnspan=2, pady=20)
        self.signup_button.grid(row=3, column=0, columnspan=2, pady=20)

    def log_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            self.root.destroy()
            self.registration_system.start_registration()
        else:
            messagebox.showerror("Error", "Invalid username or password. Please try again.")

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            if username not in self.users:
                self.users[username] = password
                messagebox.showinfo("Success", "Account created successfully. You can now log in.")
            else:
                messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        else:
            messagebox.showerror("Error", "Please enter both username and password.")

class GymMembershipRegistrationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Membership Registration System")
        self.root.configure(bg='#800080')  # Set background color to purple

        self.members = {}

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', background='#ffff00')  # Set background color for buttons to yellow

        self.name_label = ttk.Label(self.root, text="Name:", background='#800080')  # Set background color to purple
        self.name_entry = ttk.Entry(self.root)

        self.birth_date_label = ttk.Label(self.root, text="Birth Date:", background='#800080')  # Set background color to purple
        self.day_label = ttk.Label(self.root, text="Day:", background='#800080')  # Set background color to purple
        self.day_var = tk.StringVar()
        self.day_entry = ttk.Combobox(self.root, textvariable=self.day_var, values=[str(i) for i in range(1, 32)])
        self.day_entry.set("1")

        self.month_label = ttk.Label(self.root, text="Month:", background='#800080')  # Set background color to purple
        self.month_var = tk.StringVar()
        self.month_entry = ttk.Combobox(self.root, textvariable=self.month_var, values=[str(i) for i in range(1, 13)])
        self.month_entry.set("1")

        self.year_label = ttk.Label(self.root, text="Year:", background='#800080')  # Set background color to purple
        self.year_var = tk.StringVar()
        self.year_entry = ttk.Combobox(self.root, textvariable=self.year_var, values=[str(i) for i in range(1900, 2031)])
        self.year_entry.set("2022")

        self.phone_label = ttk.Label(self.root, text="Phone Number:", background='#800080')  # Set background color to purple
        self.phone_entry = ttk.Entry(self.root, validate='key', validatecommand=(self.root.register(self.validate_phone), '%P'))

        self.email_label = ttk.Label(self.root, text="Email:", background='#800080')  # Set background color to purple
        self.email_entry = ttk.Entry(self.root)

        self.membership_type_label = ttk.Label(self.root, text="Membership Type:", background='#800080')  # Set background color to purple
        self.membership_type_var = tk.StringVar()
        self.membership_type_var.set("Basic")
        self.membership_type_menu = ttk.Combobox(self.root, textvariable=self.membership_type_var, values=["Basic", "Premium", "VIP"])

        self.confirmation_label = ttk.Label(self.root, text="Registration Confirmation:", background='#800080')  # Set background color to purple
        self.confirmation_var = tk.StringVar()
        self.confirmation_display = ttk.Label(self.root, textvariable=self.confirmation_var, background='#800080')  # Set background color to purple

        self.user_info_label = ttk.Label(self.root, text="User Information:", background='#800080')  # Set background color to purple
        self.user_info_display = ttk.Label(self.root, text="", background='#800080')  # Set background color to purple

        self.register_button = ttk.Button(self.root, text="Register", command=self.register_member, style='TButton')  # Apply a style for the button
        self.exit_button = ttk.Button(self.root, text="Exit", command=self.root.destroy, style='TButton')  # Apply a style for the button

        self.name_label.grid(row=0, column=0, pady=10, sticky=tk.E)
        self.name_entry.grid(row=0, column=1, pady=10)

        self.birth_date_label.grid(row=1, column=0, pady=10, sticky=tk.E)
        self.day_label.grid(row=1, column=1, pady=10)
        self.day_entry.grid(row=1, column=2, pady=10)
        ttk.Label(self.root, text="-", background='#800080').grid(row=1, column=3, pady=10)
        self.month_label.grid(row=1, column=4, pady=10)
        self.month_entry.grid(row=1, column=5, pady=10)
        ttk.Label(self.root, text="-", background='#800080').grid(row=1, column=6, pady=10)
        self.year_label.grid(row=1, column=7, pady=10)
        self.year_entry.grid(row=1, column=8, pady=10)

        self.phone_label.grid(row=2, column=0, pady=10, sticky=tk.E)
        self.phone_entry.grid(row=2, column=1, pady=10)

        self.email_label.grid(row=3, column=0, pady=10, sticky=tk.E)
        self.email_entry.grid(row=3, column=1, pady=10)

        self.membership_type_label.grid(row=4, column=0, pady=10, sticky=tk.E)
        self.membership_type_menu.grid(row=4, column=1, pady=10)

        self.confirmation_label.grid(row=5, column=0, columnspan=9, pady=10)
        self.confirmation_display.grid(row=6, column=0, columnspan=9, pady=10)

        self.user_info_label.grid(row=7, column=0, columnspan=9, pady=10)
        self.user_info_display.grid(row=8, column=0, columnspan=9, pady=10)

        self.register_button.grid(row=9, column=0, columnspan=9, pady=20)
        self.exit_button.grid(row=10, column=0, columnspan=9, pady=20)

    def validate_phone(self, value):
        return value.isdigit() and (len(value) <= 11 or value == "")

    def register_member(self):
        name = self.name_entry.get()
        day = self.day_entry.get()
        month = self.month_entry.get()
        year = self.year_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        membership_type = self.membership_type_var.get()

        birth_date_str = f"{day}-{month}-{year}"

        if name and day and month and year and phone and email:
            try:
                birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y").date()
                age = self.calculate_age(birth_date)
            except ValueError:
                messagebox.showerror("Error", "Invalid birth date format. Please use DD-MM-YYYY.")
                return

            if email not in self.members:
                self.members[email] = {'name': name, 'phone': phone, 'age': age, 'membership_type': membership_type}
                confirmation_text = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nBirth Date: {birth_date_str}\nAge: {age}\nMembership Type: {membership_type}\n\nRegistration Successful!"
                self.confirmation_var.set(confirmation_text)

                # Display user information
                user_info_text = f"User Information:\nName: {name}\nAge: {age}\nPhone: {phone}\nEmail: {email}\nMembership Type: {membership_type}"
                self.user_info_display.config(text=user_info_text)

                messagebox.showinfo("Success", "Registration successful!")
                self.reset_form()
            else:
                messagebox.showerror("Error", "Email already registered. Please use a different email.")
        else:
            messagebox.showerror("Error", "Please enter all required information.")

    def calculate_age(self, birth_date):
        today = datetime.now().date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def reset_form(self):
        self.name_entry.delete(0, tk.END)
        self.day_entry.set("1")
        self.month_entry.set("1")
        self.year_entry.set("2022")
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.membership_type_menu.set("Basic")
        self.confirmation_var.set("")
        self.user_info_display.config(text="")

    def start_registration(self):
        self.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")  # Set the initial dimensions of the registration window
    root.withdraw()  # Hide the root window initially

    registration_system = GymMembershipRegistrationSystem(tk.Toplevel(root))
    authentication_system = AuthenticationSystem(root, registration_system)

    root.mainloop()