# 🔐 Advanced Password Tool (Python + Tkinter)

A complete and beginner-friendly Python application that helps you:
- Check password strength  
- Get suggestions to improve weak passwords  
- Generate strong random passwords  
- Save passwords securely (AES encryption)  
- View password history (decrypted only inside the app)  

This project uses **Tkinter** for GUI and **Fernet (AES encryption)** from the `cryptography` library to protect saved passwords.

---

## 🚀 Features

### ✓ Password Strength Checker  
Analyzes password strength based on:
- Length  
- Uppercase letters  
- Lowercase letters  
- Numbers  
- Special characters  

Shows strength as **Weak**, **Medium**, or **Strong**.

---

### ✓ Smart Suggestions  
If a password is weak, the app suggests improvements like:
- Use at least 8 characters  
- Add uppercase letters  
- Add lowercase letters  
- Include numbers  
- Add special characters  

---

### ✓ Strong Password Generator  
- Generates secure random passwords  
- Uses letters, numbers, and special characters  
- One-click insert into the input field  

---

### ✓ Secure Password Saving (AES Encryption)
Saved passwords are encrypted using the **Fernet encryption** system:
- A file named `secret.key` stores the encryption key  
- Passwords are stored in an encrypted file `passwords.enc`  
- You can only decrypt/view them through the app  

This keeps your stored passwords private and secure.

---

### ✓ Password History Viewer  
Displays all saved passwords after decrypting them inside a popup window.

---

