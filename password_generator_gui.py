import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        all_chars = lower + upper + digits + symbols

        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols)
        ]

        password += random.choices(all_chars, k=length - 4)
        random.shuffle(password)

        final_password = ''.join(password)
        password_display.delete(0, tk.END)
        password_display.insert(0, final_password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number ≥ 4.")

def copy_to_clipboard():
    generated_password = password_display.get()
    if generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x200")

tk.Label(root, text="Enter password length (≥ 4):").pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)

password_display = tk.Entry(root, width=35, font=("Arial", 12))
password_display.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
