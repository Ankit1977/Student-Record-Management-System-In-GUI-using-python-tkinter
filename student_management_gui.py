import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # For image resizing
import os

students = []

def add_student():
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()
    year = year_entry.get()
    roll = roll_entry.get()
    college = college_entry.get()

    if name and course and semester and year and roll and college:
        for student in students:
            if student[4] == roll:
                messagebox.showwarning("Duplicate", "Roll No already exists!")
                return
        students.append([name, course, semester, year, roll, college])
        update_treeview()
        clear_entries()
        messagebox.showinfo("Success", "Student added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields!")

def update_treeview():
    tree.delete(*tree.get_children())
    for student in students:
        tree.insert("", tk.END, values=student)

def delete_student():
    selected = tree.selection()
    if selected:
        index = tree.index(selected)
        del students[index]
        update_treeview()
        messagebox.showinfo("Deleted", "Student deleted.")
    else:
        messagebox.showwarning("Error", "Please select a record.")

def search_student():
    roll = search_entry.get()
    for student in students:
        if student[4] == roll:
            name_entry.delete(0, tk.END)
            course_entry.delete(0, tk.END)
            semester_entry.delete(0, tk.END)
            year_entry.delete(0, tk.END)
            roll_entry.delete(0, tk.END)
            college_entry.delete(0, tk.END)

            name_entry.insert(0, student[0])
            course_entry.insert(0, student[1])
            semester_entry.insert(0, student[2])
            year_entry.insert(0, student[3])
            roll_entry.insert(0, student[4])
            college_entry.insert(0, student[5])
            search_entry.delete(0, tk.END)
            messagebox.showinfo("Found", "Student data loaded for update.")
            return
    messagebox.showwarning("Not Found", "Student with this Roll No not found.")

def update_student():
    roll = roll_entry.get()
    for i, student in enumerate(students):
        if student[4] == roll:
            students[i] = [
                name_entry.get(),
                course_entry.get(),
                semester_entry.get(),
                year_entry.get(),
                roll_entry.get(),
                college_entry.get()
            ]
            update_treeview()
            clear_entries()
            messagebox.showinfo("Updated", "Student record updated.")
            return
    messagebox.showwarning("Not Found", "Student with this Roll No not found.")

def clear_entries():
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    college_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Student Record Management System")
root.geometry("950x650")
root.resizable(False, False)

# Set icon image
if os.path.exists("background.png"):
    icon_img = ImageTk.PhotoImage(Image.open("background.png").resize((32, 32)))
    root.iconphoto(False, icon_img)

# Add background
bg_img = Image.open("background.png").resize((950, 650))
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Overlay frame
overlay = tk.Frame(root, bg="#000000", bd=2)
overlay.place(x=10, y=10, width=930, height=630)

# Title
tk.Label(overlay, text="Student Record Management System", font=("Verdana", 18, "bold"),
         bg="#ffff99", fg="black").pack(pady=10, fill=tk.X)

# Input Frame
input_frame = tk.Frame(overlay, bg="#000000")
input_frame.pack(pady=10)

def create_label_entry(frame, text, row, col):
    label = tk.Label(frame, text=text, font=("Arial", 12, "bold"), bg="#000000", fg="#ffffff")
    label.grid(row=row, column=col, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame, font=("Arial", 12), bg="#333344", fg="white", insertbackground="white")
    entry.grid(row=row, column=col+1, padx=10, pady=5)
    return entry

name_entry = create_label_entry(input_frame, "Name:", 0, 0)
course_entry = create_label_entry(input_frame, "Course:", 0, 2)
semester_entry = create_label_entry(input_frame, "Semester:", 1, 0)
year_entry = create_label_entry(input_frame, "Year:", 1, 2)
roll_entry = create_label_entry(input_frame, "Roll No:", 2, 0)
college_entry = create_label_entry(input_frame, "College Name:", 2, 2)

# Buttons
button_frame = tk.Frame(overlay, bg="#000000")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", command=add_student, width=12, bg="#228B22", fg="white", cursor="hand2").grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Update", command=update_student, width=12, bg="#1E90FF", fg="white", cursor="hand2").grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Delete", command=delete_student, width=12, bg="#B22222", fg="white", cursor="hand2").grid(row=0, column=2, padx=10)
tk.Button(button_frame, text="Clear", command=clear_entries, width=12, bg="#696969", fg="white", cursor="hand2").grid(row=0, column=3, padx=10)

# Search Field
search_frame = tk.Frame(overlay, bg="#000000")
search_frame.pack(pady=5)

tk.Label(search_frame, text="Search Roll No:", font=("Arial", 12), bg="#000000", fg="white").grid(row=0, column=0, padx=5)
search_entry = tk.Entry(search_frame, font=("Arial", 12), bg="#333344", fg="white", insertbackground="white")
search_entry.grid(row=0, column=1, padx=5)
tk.Button(search_frame, text="Search", command=search_student, width=10, bg="#FFA500", fg="black", cursor="hand2").grid(row=0, column=2, padx=5)

# Treeview
tree = ttk.Treeview(overlay, columns=("Name", "Course", "Semester", "Year", "Roll", "College"), show="headings")
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#262626",
                foreground="white",
                fieldbackground="#262626",
                rowheight=25,
                font=("Arial", 11))
style.configure("Treeview.Heading",
                background="#333344",
                foreground="white",
                font=("Arial", 12, "bold"))

for col in ("Name", "Course", "Semester", "Year", "Roll", "College"):
    tree.heading(col, text=col)
    tree.column(col, width=130)

tree.pack(pady=10, fill=tk.X, padx=20)

# Footer
tk.Label(overlay, text="© 2025 Student Management | Designed by Ankit", font=("Arial", 10),
         bg="#000000", fg="#aaaaaa").pack(pady=5)

root.mainloop()
