import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

def add_task():
    task = task_entry.get()
    time = time_entry.get()
    date = cal.get_date()
    if task and time and date:
        task_listbox.insert(tk.END, f"{task} - {time} - {date}")
        task_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter task, time, and date!")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task():
    try:
        index = task_listbox.curselection()[0]
        updated_task = task_entry.get()
        updated_time = time_entry.get()
        date = cal.get_date()
        task_listbox.delete(index)
        task_listbox.insert(index, f"{updated_task} - {updated_time} - {date}")
        task_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

def mark_task_completed(event):
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        task_listbox.itemconfig(index, {'bg':'red'})
    except IndexError:
        pass

# Create the main application window
root = tk.Tk()
root.title("To-Do List App with Date and Time")
root.configure(bg='black')  # Set background color to black

# Create task and time entry fields
tk.Label(root, text="Task:", bg='black', fg='white').grid(row=0, column=0, padx=10, pady=10)
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Time:", bg='black', fg='white').grid(row=1, column=0, padx=10, pady=10)
time_entry = tk.Entry(root, width=50)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Date:", bg='black', fg='white').grid(row=2, column=0, padx=10, pady=10)
cal = Calendar(root, selectmode='day', year=2024, month=6, day=26)
cal.grid(row=2, column=1, padx=10, pady=10)

# Create task listbox
task_listbox = tk.Listbox(root, height=10, width=50, bg='black', fg='white')
task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
task_listbox.bind('<Double-1>', mark_task_completed)

# Create buttons with green background
add_button = tk.Button(root, text="Add Task", width=20, command=add_task, bg='green', fg='white')
add_button.grid(row=4, column=0, padx=5, pady=10)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task, bg='green', fg='white')
delete_button.grid(row=4, column=1, padx=5, pady=10)

update_button = tk.Button(root, text="Update Task", width=20, command=update_task, bg='green', fg='white')
update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# Start the main loop
root.mainloop()
