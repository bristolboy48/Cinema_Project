import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()
    # You can add your own logic here for authenticating the user
    if username == "your_username" and password == "your_password":
        messagebox.showinfo("Login", "Login successful!!!")
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# Function to handle registration
def register():
    username = entry_new_username.get()
    password = entry_new_password.get()

    # You can add your own logic here for user registration
    # Typically, this would involve saving the username and password securely
    # For simplicity, we'll just display a message here
    messagebox.showinfo("Registration", f"User {username} registered successfully!")

# Create the main window
root = tk.Tk()
root.title("Login/Register")

# Login Frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

label_username = tk.Label(login_frame, text="Username:")
label_username.pack()
entry_username = tk.Entry(login_frame)
entry_username.pack()

label_password = tk.Label(login_frame, text="Password:")
label_password.pack()
entry_password = tk.Entry(login_frame, show="*")  # Mask the password
entry_password.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack()

# Registration Frame
register_frame = tk.Frame(root)
register_frame.pack(pady=20)

label_new_username = tk.Label(register_frame, text="New Username:")
label_new_username.pack()
entry_new_username = tk.Entry(register_frame)
entry_new_username.pack()

label_new_password = tk.Label(register_frame, text="New Password:")
label_new_password.pack()
entry_new_password = tk.Entry(register_frame, show="*")  # Mask the password
entry_new_password.pack()

register_button = tk.Button(register_frame, text="Register", command=register)
register_button.pack()

root.mainloop()
