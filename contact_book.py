import tkinter as tk
from tkinter import messagebox, simpledialog

# In-memory contact list (you can extend this to use a file or database)
contacts = []

# Functions
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and phone number are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    messagebox.showinfo("Success", f"Contact '{name}' added.")
    clear_fields()
    view_contacts()

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def view_contacts():
    listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        listbox.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number:")
    if not query:
        return

    results = [c for c in contacts if query.lower() in c["name"].lower() or query in c["phone"]]
    listbox.delete(0, tk.END)
    if results:
        for i, contact in enumerate(results):
            listbox.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")
    else:
        messagebox.showinfo("Search", "No matching contact found.")

def update_contact():
    try:
        index = listbox.curselection()[0]
        contact = contacts[index]

        name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact["name"])
        phone = simpledialog.askstring("Update Phone", "Enter new phone:", initialvalue=contact["phone"])
        email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact["email"])
        address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact["address"])

        contacts[index] = {
            "name": name or contact["name"],
            "phone": phone or contact["phone"],
            "email": email or contact["email"],
            "address": address or contact["address"]
        }

        messagebox.showinfo("Updated", "Contact updated successfully.")
        view_contacts()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")

def delete_contact():
    try:
        index = listbox.curselection()[0]
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this contact?")
        if confirm:
            contacts.pop(index)
            messagebox.showinfo("Deleted", "Contact deleted successfully.")
            view_contacts()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("450x500")

# Input fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View All Contacts", command=view_contacts).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Update Selected", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_contact).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

root.mainloop()
