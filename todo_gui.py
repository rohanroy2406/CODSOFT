import tkinter as tk
from tkinter import messagebox
import json
import os

TODO_FILE = "todo_data.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = load_tasks()

        self.task_input = tk.Entry(root, width=40)
        self.task_input.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save)
        self.save_button.pack(pady=10)

        self.load_to_listbox()

    def load_to_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            title = task["title"]
            status = "✔️" if task["completed"] else "❌"
            self.task_listbox.insert(tk.END, f"{title} [{status}]")

    def add_task(self):
        title = self.task_input.get().strip()
        if title:
            self.tasks.append({"title": title, "completed": False})
            self.task_input.delete(0, tk.END)
            self.load_to_listbox()
        else:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.load_to_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks.pop(index)
            self.load_to_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    def save(self):
        save_tasks(self.tasks)
        messagebox.showinfo("Save Successful", "Tasks have been saved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
