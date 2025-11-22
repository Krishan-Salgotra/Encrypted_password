import re
import random
import string
import tkinter as tk
from tkinter import messagebox, Toplevel, Text, END
from cryptography.fernet import Fernet
import os


# ------------------------------
# Encryption Key Setup
# ------------------------------
KEY_FILE = "secret.key"
PASSWORD_FILE = "passwords.enc"

# Create a key if not exists
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

key = load_key()
cipher = Fernet(key)


# ------------------------------
# Save password (Encrypted)
# ------------------------------
def save_password(password):
    encrypted = cipher.encrypt(password.encode())

    with open(PASSWORD_FILE, "ab") as f:
        f.write(encrypted + b"\n")

    messagebox.showinfo("Saved", "Password saved securely!")


# ------------------------------
# Load password history (Decrypted)
# ------------------------------
def show_history():
    if not os.path.exists(PASSWORD_FILE):
        messagebox.showinfo("History", "No saved passwords yet.")
        return

    window = Toplevel(root)
    window.title("Password History")
    window.geometry("400x400")

    text_area = Text(window, font=("Arial", 12))
    text_area.pack(fill="both", expand=True)

    with open(PASSWORD_FILE, "rb") as f:
        lines = f.readlines()

    text_area.insert(END, "Saved Passwords:\n\n")

    for line in lines:
        try:
            decrypted = cipher.decrypt(line.strip()).decode()
            text_area.insert(END, f"- {decrypted}\n")
        except:
            pass


# ------------------------------
# Password Strength Checker
# ------------------------------
def check_password_strength(password):
    strength_points = 0
    suggestions = []

    if len(password) >= 8:
        strength_points += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        suggestions.append("Include numbers (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        suggestions.append("Add special characters (!@#$%).")

    if strength_points <= 2:
        level = "Weak"
    elif strength_points == 3 or strength_points == 4:
        level = "Medium"
    else:
        level = "Strong"

    return level, suggestions


# ------------------------------
# Strong Password Generator
# ------------------------------
def generate_password():
    length = 12
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)


# ------------------------------
# GUI: Strength Button
# ------------------------------
def check_strength():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Error", "Please enter a password.")
        return

    level, suggestions = check_password_strength(password)
    result_label.config(text=f"Strength: {level}")

    suggestions_text.delete("1.0", tk.END)

    if level != "Strong":
        suggestions_text.insert(tk.END, "Suggestions:\n")
        for s in suggestions:
            suggestions_text.insert(tk.END, f"- {s}\n")
    else:
        suggestions_text.insert(tk.END, "Strong password! No suggestions.")


# ------------------------------
# Tkinter GUI Setup
# ------------------------------
root = tk.Tk()
root.title("Password Strength Tool")
root.geometry("460x500")
root.resizable(False, False)

title_label = tk.Label(root, text="🔐 Advanced Password Tool", font=("Arial", 17, "bold"))
title_label.pack(pady=10)

entry_password = tk.Entry(root, width=32, font=("Arial", 14), show="*")
entry_password.pack(pady=10)

btn_check = tk.Button(root, text="Check Strength", font=("Arial", 12), command=check_strength)
btn_check.pack(pady=5)

btn_generate = tk.Button(root, text="Generate Strong Password", font=("Arial", 12), command=generate_password)
btn_generate.pack(pady=5)

btn_save = tk.Button(root, text="Save Password Securely", font=("Arial", 12),
                     command=lambda: save_password(entry_password.get()))
btn_save.pack(pady=5)

btn_history = tk.Button(root, text="View Password History", font=("Arial", 12), command=show_history)
btn_history.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

suggestions_text = tk.Text(root, height=8, width=50, font=("Arial", 11))
suggestions_text.pack(pady=10)

root.mainloop()
s