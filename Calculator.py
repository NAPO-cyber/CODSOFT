import tkinter as tk

# main functions
def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# The GUI
root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# layout accordance with real calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    def handler(x=button):
        if x == '=':
            calculate()
        else:
            button_click(x)
    b = tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), command=handler)
    b.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# AC (all clear) button
clear_button = tk.Button(root, text="AC", width=22, height=2, font=("Arial", 14), command=clear)
clear_button.grid(row=row_val, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
