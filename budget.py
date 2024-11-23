import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

# Global variables
profiles = {}  # To store profile name-PIN pairs
current_profile = None  # Track the currently logged-in profile
data_files_dir = "user_data"  # Directory to save individual profile files

# Ensure directory for profile files exists
if not os.path.exists(data_files_dir):
    os.makedirs(data_files_dir)

def save_profiles_data():
    """Save profile credentials to a file."""
    with open("profiles.txt", "w") as file:
        for profile_name, pin in profiles.items():
            file.write(f"{profile_name}:{pin}\n")

def load_profiles_data():
    """Load profile credentials from a file."""
    global profiles
    if os.path.exists("profiles.txt"):
        with open("profiles.txt", "r") as file:
            for line in file:
                profile_name, pin = line.strip().split(":")
                profiles[profile_name] = pin

def save_budget_data(profile):
    """Save budget data for the current profile."""
    file_path = os.path.join(data_files_dir, f"{profile}_budget.csv")
    budget_data.to_csv(file_path, index=False)

def load_budget_data(profile):
    """Load budget data for the current profile."""
    global budget_data
    file_path = os.path.join(data_files_dir, f"{profile}_budget.csv")
    if os.path.exists(file_path):
        budget_data = pd.read_csv(file_path)
    else:
        budget_data = pd.DataFrame(columns=["Date", "Description", "Category", "Amount"])

# Load profile credentials at the start
load_profiles_data()

# Initialize an empty DataFrame for budget data
budget_data = pd.DataFrame(columns=["Date", "Description", "Category", "Amount"])

# Tkinter GUI
root = tk.Tk()
root.title("Budget App")

# Set background color for a fresh look
root.configure(bg="#d0e6f6")  # Soft pastel blue

def login():
    """Handle profile login."""
    global current_profile
    profile_name = profile_name_entry.get()
    pin = pin_entry.get()
    if profile_name in profiles and profiles[profile_name] == pin:
        current_profile = profile_name
        load_budget_data(current_profile)
        messagebox.showinfo("Login Successful", f"Welcome, {profile_name}!")
        switch_to_main_screen()
    else:
        messagebox.showerror("Login Failed", "Invalid profile name or PIN.")

def register():
    """Handle profile registration."""
    profile_name = profile_name_entry.get()
    pin = pin_entry.get()
    if profile_name in profiles:
        messagebox.showerror("Registration Failed", "Profile name already exists.")
    else:
        profiles[profile_name] = pin
        save_profiles_data()
        messagebox.showinfo("Registration Successful", "Profile registered successfully!")

def add_transaction_gui():
    """Add transaction via GUI."""
    date = date_entry.get()
    description = desc_entry.get()
    category = category_entry.get()
    try:
        amount = float(amount_entry.get())
        new_transaction = pd.DataFrame([[date, description, category, amount]], columns=["Date", "Description", "Category", "Amount"])
        global budget_data
        budget_data = pd.concat([budget_data, new_transaction], ignore_index=True)
        save_budget_data(current_profile)
        messagebox.showinfo("Success", "Transaction added successfully!")
        view_transactions()
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered.")

def view_transactions():
    """View all transactions."""
    for item in transaction_tree.get_children():
        transaction_tree.delete(item)
    for _, row in budget_data.iterrows():
        transaction_tree.insert("", "end", values=list(row))

def switch_to_main_screen():
    """Switch to the main budget screen."""
    login_frame.pack_forget()
    main_frame.pack()

# Login Frame
login_frame = tk.Frame(root, bg="#d0e6f6", padx=20, pady=20)  # Add padding for better spacing
login_frame.pack()

tk.Label(login_frame, text="Profile Name:", font=("Arial", 14), bg="#d0e6f6").grid(row=0, column=0, pady=10, sticky="e")
profile_name_entry = tk.Entry(login_frame, font=("Arial", 14), width=20)
profile_name_entry.grid(row=0, column=1, pady=10)

tk.Label(login_frame, text="PIN:", font=("Arial", 14), bg="#d0e6f6").grid(row=1, column=0, pady=10, sticky="e")
pin_entry = tk.Entry(login_frame, font=("Arial", 14), width=20, show="*")
pin_entry.grid(row=1, column=1, pady=10)

tk.Button(login_frame, text="Login", font=("Arial", 14), command=login, bg="#1a73e8", fg="white", width=12).grid(row=2, column=0, pady=10)
tk.Button(login_frame, text="Register", font=("Arial", 14), command=register, bg="#1a73e8", fg="white", width=12).grid(row=2, column=1, pady=10)

# Main Frame
main_frame = tk.Frame(root, bg="#d0e6f6")

tk.Label(main_frame, text="Date (YYYY-MM-DD):", font=("Arial", 14), bg="#d0e6f6").grid(row=0, column=0, pady=5)
date_entry = tk.Entry(main_frame, font=("Arial", 14), width=20)
date_entry.grid(row=0, column=1, pady=5)

tk.Label(main_frame, text="Description:", font=("Arial", 14), bg="#d0e6f6").grid(row=1, column=0, pady=5)
desc_entry = tk.Entry(main_frame, font=("Arial", 14), width=20)
desc_entry.grid(row=1, column=1, pady=5)

tk.Label(main_frame, text="Category:", font=("Arial", 14), bg="#d0e6f6").grid(row=2, column=0, pady=5)
category_entry = tk.Entry(main_frame, font=("Arial", 14), width=20)
category_entry.grid(row=2, column=1, pady=5)

tk.Label(main_frame, text="Amount:", font=("Arial", 14), bg="#d0e6f6").grid(row=3, column=0, pady=5)
amount_entry = tk.Entry(main_frame, font=("Arial", 14), width=20)
amount_entry.grid(row=3, column=1, pady=5)

tk.Button(main_frame, text="Add Transaction", font=("Arial", 14), command=add_transaction_gui, bg="#1a73e8", fg="white", width=20).grid(row=4, columnspan=2, pady=10)
tk.Button(main_frame, text="View Transactions", font=("Arial", 14), command=view_transactions, bg="#1a73e8", fg="white", width=20).grid(row=5, columnspan=2, pady=10)

# Transaction Treeview
transaction_tree = ttk.Treeview(main_frame, columns=("Date", "Description", "Category", "Amount"), show="headings", height=10)
transaction_tree.heading("Date", text="Date")
transaction_tree.heading("Description", text="Description")
transaction_tree.heading("Category", text="Category")
transaction_tree.heading("Amount", text="Amount")
transaction_tree.grid(row=6, columnspan=2, pady=10)

# Start the app
root.mainloop()
