import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from database import add_application, get_all_applications
from email_automation import send_followup_email

def add_job():
    recruiter_name = entry_name.get()
    email = entry_email.get()
    date_applied = entry_date.get()
    followup_prompt = entry_prompt.get()

    if recruiter_name and email and date_applied:
        add_application(recruiter_name, email, date_applied, followup_prompt)
        load_data()
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        entry_prompt.delete(0, tk.END)
        messagebox.showinfo("Success", "Job application added successfully")
    else:
        messagebox.showwarning("Error", "Please fill in all required fields")

def load_data():
    for row in tree.get_children():
        tree.delete(row)
    applications = get_all_applications()
    for app in applications:
        tree.insert('', tk.END, values=app)

def send_email():
    selected_item = tree.focus()
    if selected_item:
        item_values = tree.item(selected_item, 'values')
        email = item_values[2]
        prompt = item_values[4]
        subject = f"Follow-up on your application"
        send_followup_email(email, subject, prompt)
        messagebox.showinfo("Success", f"Follow-up email sent to {email}")
    else:
        messagebox.showwarning("Warning", "No application selected")

# Creating the main window
window = tk.Tk()
window.title("Job Application Tracker")

# Form inputs
tk.Label(window, text="Recruiter Name").grid(row=0, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

tk.Label(window, text="Recruiter Email").grid(row=1, column=0)
entry_email = tk.Entry(window)
entry_email.grid(row=1, column=1)

tk.Label(window, text="Date Applied").grid(row=2, column=0)
entry_date = tk.Entry(window)
entry_date.grid(row=2, column=1)

tk.Label(window, text="Follow-up Prompt").grid(row=3, column=0)
entry_prompt = tk.Entry(window)
entry_prompt.grid(row=3, column=1)

tk.Button(window, text="Add Job", command=add_job).grid(row=4, column=0, columnspan=2)

# Table for displaying job applications
columns = ('ID', 'Recruiter Name', 'Email', 'Date Applied', 'Follow-up Prompt')
tree = ttk.Treeview(window, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=2)

tk.Button(window, text="Send Follow-up Email", command=send_email).grid(row=6, column=0, columnspan=2)

load_data()
window.mainloop()
