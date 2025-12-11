import re
import tkinter as tk
from tkinter import messagebox

COMMON_PASSWORDS = {
    "123456","password","12345678","qwerty","abc123","111111","1234567",
    "iloveyou","password1","admin","welcome"
}

def check_password_strength(password):
    suggestions = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers 0-9.")

    if re.search(r"[@#$%^&*!()_+]", password):
        score += 1
    else:
        suggestions.append("Add special characters (@,#,$, etc).")

    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid common passwords like 'password' or '123456'.")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions

def check():
    pwd = entry.get()
    strength, suggestions = check_password_strength(pwd)

    msg = f"Password Strength: {strength}\n\nSuggestions:\n"
    for s in suggestions:
        msg += "- " + s + "\n"

    messagebox.showinfo("Result", msg)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

tk.Button(root, text="Check Strength", command=check).pack()

root.mainloop()
