import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Select Operation:").pack(pady=5)

# Buttons for operations
tk.Button(root, text="+", width=10, command=lambda: calculate('+')).pack(pady=2)
tk.Button(root, text="-", width=10, command=lambda: calculate('-')).pack(pady=2)
tk.Button(root, text="*", width=10, command=lambda: calculate('*')).pack(pady=2)
tk.Button(root, text="/", width=10, command=lambda: calculate('/')).pack(pady=2)

# Result display
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
