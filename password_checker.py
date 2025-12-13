import tkinter as tk
from tkinter import ttk
import re

# Check strength function
def check_strength():
    password = entry.get()
    strength = 0
    remarks = ""

    # Strength Conditions
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "• At least 8 characters needed\n"

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "• Add one uppercase letter (A-Z)\n"

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "• Add one lowercase letter (a-z)\n"

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "• Add one digit (0-9)\n"

    if re.search(r"[!@#$%^&*()_+=\-?]", password):
        strength += 1
    else:
        remarks += "• Add one special character (!,@,#,$,?)\n"

    # Strength Display
    if strength == 5:
        result_label.config(text="Strong Password", foreground="#00b33c")
        strength_bar["value"] = 100
    elif strength >= 3:
        result_label.config(text="Medium Password", foreground="#ff9900")
        strength_bar["value"] = 60
    else:
        result_label.config(text="Weak Password", foreground="#ff3333")
        strength_bar["value"] = 25

    remarks_text.config(state="normal")
    remarks_text.delete("1.0", tk.END)
    remarks_text.insert(tk.END, remarks)
    remarks_text.config(state="disabled")


# Window Setup
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("480x420")
window.config(bg="#E9EEF3")

# Center Frame (Card Style)
frame = tk.Frame(window, bg="white", bd=0, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.configure(width=380, height=360)

# Title
title = tk.Label(frame, text="🔐 Password Strength Checker", 
                 font=("Segoe UI", 16, "bold"), bg="white")
title.place(relx=0.5, rely=0.12, anchor="center")

# Label
label = tk.Label(frame, text="Enter Password:", font=("Segoe UI", 11), bg="white")
label.place(relx=0.10, rely=0.25)

# Entry
entry = tk.Entry(frame, width=28, font=("Segoe UI", 12), show="*",
                 bd=1, relief="solid")
entry.place(relx=0.10, rely=0.32)

# Button
button = tk.Button(frame, text="Check Strength", font=("Segoe UI", 11, "bold"),
                   bg="#4A6CF7", fg="white", relief="flat",
                   padx=10, pady=5, command=check_strength, cursor="hand2")
button.place(relx=0.10, rely=0.42)

# Result Label
result_label = tk.Label(frame, text="Password Strength: ", 
                        font=("Segoe UI", 12, "bold"), bg="white")
result_label.place(relx=0.10, rely=0.53)

# Strength Progress Bar
style = ttk.Style()
style.theme_use("clam")
style.configure("blue.Horizontal.TProgressbar", troughcolor="#D9E1E8", 
                bordercolor="white", background="#4A6CF7", lightcolor="#4A6CF7", darkcolor="#4A6CF7")
strength_bar = ttk.Progressbar(frame, orient="horizontal", length=250,
                               style="blue.Horizontal.TProgressbar", mode="determinate")
strength_bar.place(relx=0.10, rely=0.60)

# Remarks
remarks_label = tk.Label(frame, text="Suggestions:", font=("Segoe UI", 11, "bold"), bg="white")
remarks_label.place(relx=0.10, rely=0.72)

remarks_text = tk.Text(frame, width=34, height=5, font=("Segoe UI", 10),
                       bd=1, relief="solid", state="disabled")
remarks_text.place(relx=0.10, rely=0.80)


window.mainloop()
