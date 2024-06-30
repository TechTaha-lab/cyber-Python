from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import re

def on_click():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path.endswith(".txt"):
        entrypath.delete(0, END)
        entrypath.insert(0, file_path)
        display_file_contents(file_path)
    else:
        messagebox.showerror("Error", "The file should be a TXT file. Other file types are not acceptable.")

def display_file_contents(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        textarea.delete("1.0", "end")
        textarea.insert("end", file_contents)

def scan_passwords(target_password):
    file_path = entrypath.get()
    with open(file_path, "r") as file:
        for password in file:
            password = password.strip()  # Remove leading/trailing whitespaces
            if password == target_password:
                return password
    return None

def attack():
    target = entryname.get()
    if target.startswith("http://") or target.startswith("https://"):
        textarea.insert("end", "You entered a website: " + target + "\n")
    else:
        textarea.insert("end", "You entered an account: " + target + "\n")
    target_password = entryname.get()
    found_password = scan_passwords(target_password)
    if found_password:
        textarea.insert("end", "Correct password: " + found_password + " (Status: Correct)\n")
    else:
        textarea.insert("end", "Password not found.\n")

def exitsprogram():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()
    else:
        root.mainloop()

root = Tk()
root.geometry("800x500+260+80")
root.title("Brute force any Target")
root.iconbitmap("download.ico")
root.resizable(False, False)

definitionlabel = Label(root, text="Brute force any Target", fg="#333", bg="whitesmoke", font=("Verdana", 13), padx=20, pady=20)
definitionlabel.pack(fill=X)

leftframe = Frame(root)
leftframe.place(x=0, y=63, width=250, height=460)

pythonphoto = PhotoImage(file="images1.png")
pythonlabel = Label(leftframe, image=pythonphoto)
pythonlabel.place(x=30, y=50)

namelinklabel = Label(leftframe, text="Name or target link:", fg="#222", font=("Verdana", 11))
namelinklabel.place(x=4, y=190)
entryname = Entry(leftframe)
entryname.place(x=4, y=220, width=220, height=30)

labelshoose = Label(leftframe, text="Password list file:", fg="#222", font=("Verdana", 11))
labelshoose.place(x=4, y=260)
entrypath = Entry(leftframe)
entrypath.place(x=4, y=290, width=220, height=30)

btnshoose = Button(leftframe, text="Choose file", fg="white", bg="royalblue", font=("Verdana", 10), cursor="hand2", command=on_click, foreground="white")
btnshoose.place(x=4, y=330, width=220, height=35)

buttons2 = Button(leftframe, text="Start brute force", fg="white", bg="#333", font=("Verdana", 10), cursor="hand2", foreground="white", command=attack)
buttons2.place(x=4, y=365, width=220, height=35)

exitsbutton = Button(leftframe, text="Exit", fg="white", bg="red", font=("Verdana", 11), cursor="hand2", command=exitsprogram, foreground="white")
exitsbutton.place(x=3, y=400, width=220, height=35)

rightframe = Frame(root, background="white")
rightframe.place(x=250, y=65, width=550, height=470)

textarea = Text(rightframe, padx=10, pady=10)
textarea.place(x=0, y=0, width=550, height=470)

root.mainloop()
