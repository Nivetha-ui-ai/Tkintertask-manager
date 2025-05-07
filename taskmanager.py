import tkinter as tk
from tkinter import END

# Create main window
root = tk.Tk()
root.title("📝 Simple Task Manager")
root.geometry("300x400")

# Task list (Listbox)
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=20)

# Entry widget for new task
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

# Add button
add_button = tk.Button(root, text="Add Task")
add_button.pack(pady=5)

# Delete button
delete_button = tk.Button(root, text="Delete Selected")
delete_button.pack(pady=5)

# Define add task behavior directly
def on_add_click():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

# Define delete task behavior directly
def on_delete_click():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)

# Link buttons to the logic
add_button.config(command=on_add_click)
delete_button.config(command=on_delete_click)

# Start the app
root.mainloop()
