import os
import tkinter as tk
from tkinter import messagebox

file = 'tasks.py'

def show_tasks():
    listbox.delete(0, tk.END)
    if os.path.exists(file):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        for task in lines:
            listbox.insert(tk.END, task.strip())

def add_task():
    task = entry.get()
    if task != "":
        f = open(file, 'a')
        f.write(task + "\n")
        f.close()
        entry.delete(0, tk.END)
        show_tasks()
        messagebox.showinfo("Done", "Task added.")
    else:
        messagebox.showwarning("Error", "Please type something.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks = list(listbox.get(0, tk.END))
        tasks.pop(selected)
        f = open(file, 'w')
        for task in tasks:
            f.write(task + "\n")
        f.close()
        show_tasks()
        messagebox.showinfo("Done", "Task deleted.")
    except:
        messagebox.showwarning("Error", "Select a task to delete.")

def clear_tasks():
    answer = messagebox.askyesno("Confirm", "Are you sure to clear all tasks?")
    if answer:
        f = open(file, 'w')
        f.close()
        show_tasks()
        messagebox.showinfo("Cleared", "All tasks cleared.")

# GUI
root = tk.Tk()
root.title("Simple To-Do List")
root.configure(bg="#222222")

FONT = ("Arial", 10, "bold")

button_style = {
    "bg": "#444444",
    "fg": "white",
    "activebackground": "#666666",
    "activeforeground": "white",
    "relief": "flat",
    "bd": 0,
    "font": FONT,
    "padx": 10,
    "pady": 5,
    "highlightbackground": "#666666",
    "highlightthickness": 2
}

listbox = tk.Listbox(root, width=50, height=15, bg="#333333", fg="white",
                     selectbackground="#555555", font=FONT)
listbox.pack(pady=10)

entry = tk.Entry(root, width=40, bg="#444444", fg="white",
                 insertbackground='white', font=FONT)
entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#222222")
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", command=add_task, **button_style)
add_button.pack(pady=5)

delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_task, **button_style)
delete_button.pack(pady=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks, **button_style)
clear_button.pack(pady=5)

exit_button = tk.Button(button_frame, text="Exit", command=root.destroy, **button_style)
exit_button.pack(pady=5)

show_tasks()

root.mainloop()
