import tkinter as tk
from tkinter import messagebox

students = []

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    dept = dept_entry.get()
    marks = marks_entry.get()

    if name == "" or roll == "" or dept == "" or marks == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    student = f"Roll: {roll}, Name: {name}, Dept: {dept}, Marks: {marks}"
    students.append(student)

    listbox.insert(tk.END, student)
    clear_fields()

def delete_student():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a student to delete")
        return

    index = selected[0]
    listbox.delete(index)
    students.pop(index)

def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

def show_all():
    listbox.delete(0, tk.END)

    for student in students:
        listbox.insert(tk.END, student)

def search_student():
    roll = roll_entry.get()

    if roll == "":
        messagebox.showwarning("Warning", "Enter roll number to search")
        return

    listbox.delete(0, tk.END)

    found = False
    for student in students:
        if f"Roll: {roll}," in student:
            listbox.insert(tk.END, student)
            found = True

    if not found:
        messagebox.showinfo("Result", "Student not found")

# Main window
window = tk.Tk()
window.title("Student Management System")
window.geometry("600x500")

title_label = tk.Label(window, text="Student Management System", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Roll No").grid(row=1, column=0, padx=10, pady=5)
roll_entry = tk.Entry(frame)
roll_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Department").grid(row=2, column=0, padx=10, pady=5)
dept_entry = tk.Entry(frame)
dept_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Marks").grid(row=3, column=0, padx=10, pady=5)
marks_entry = tk.Entry(frame)
marks_entry.grid(row=3, column=1, padx=10, pady=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Student", width=15, command=add_student).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Delete Student", width=15, command=delete_student).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Search", width=15, command=search_student).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Show All", width=15, command=show_all).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Clear Fields", width=15, command=clear_fields).grid(row=1, column=1, columnspan=2, pady=10)

listbox = tk.Listbox(window, width=80, height=12)
listbox.pack(pady=10)

window.mainloop()
