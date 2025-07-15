import tkinter as tk
from tkinter import messagebox

contacts = {}  # dictionary to store contacts

# functions
def add():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts[name] = [phone, email, address]
        messagebox.showinfo("Success", "Contact added!")
        clear()
        hide_contacts()
    else:
        messagebox.showwarning("Error", "Name and Phone required.")

def view():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details[0]}")
    contact_list.grid(row=7, column=0, columnspan=2, pady=10)  # show listbox

def search():
    name = name_entry.get()
    found = False
    contact_list.delete(0, tk.END)
    for key in contacts:
        if name.lower() in key.lower():
            contact_list.insert(tk.END, f"{key} - {contacts[key][0]}")
            found = True
    if not found:
        messagebox.showinfo("Not Found", "No contact found.")
    contact_list.grid(row=7, column=0, columnspan=2, pady=10)  # show listbox

def update():
    name = name_entry.get()
    if name in contacts:
        contacts[name] = [phone_entry.get(), email_entry.get(), address_entry.get()]
        messagebox.showinfo("Updated", "Contact updated!")
        clear()
        hide_contacts()
    else:
        messagebox.showwarning("Error", "Contact not found.")

def delete():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", "Contact deleted!")
        clear()
        hide_contacts()
    else:
        messagebox.showwarning("Error", "Contact not found.")

def clear():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def hide_contacts():
    contact_list.grid_remove()  # hides the contact list


# the GUI
root = tk.Tk()
root.title("Contact Book")
root.configure(bg="#FADBD8")  # light soothing red

FONT = ("Arial", 10)

label_style = {"bg": "#FADBD8", "font": FONT}
entry_style = {"font": FONT}
button_style = {"bg": "#E6B0AA", "fg": "black", "font": FONT, "width": 15, "activebackground": "#CD6155"}

# labels and entry fields
tk.Label(root, text="Name:", **label_style).grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(root, **entry_style)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:", **label_style).grid(row=1, column=0, padx=5, pady=5, sticky="w")
phone_entry = tk.Entry(root, **entry_style)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:", **label_style).grid(row=2, column=0, padx=5, pady=5, sticky="w")
email_entry = tk.Entry(root, **entry_style)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Address:", **label_style).grid(row=3, column=0, padx=5, pady=5, sticky="w")
address_entry = tk.Entry(root, **entry_style)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# buttons
tk.Button(root, text="Add Contact", command=add, **button_style).grid(row=4, column=0, pady=5)
tk.Button(root, text="View Contacts", command=view, **button_style).grid(row=4, column=1, pady=5)
tk.Button(root, text="Search Contact", command=search, **button_style).grid(row=5, column=0, pady=5)
tk.Button(root, text="Update Contact", command=update, **button_style).grid(row=5, column=1, pady=5)
tk.Button(root, text="Delete Contact", command=delete, **button_style).grid(row=6, column=0, pady=5)
tk.Button(root, text="Clear Fields", command=clear, **button_style).grid(row=6, column=1, pady=5)

contact_list = tk.Listbox(root, width=40, font=FONT)

hide_contacts() # keep the contacts hidden

root.mainloop()
