import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

def generate_password_list():
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '!@#$%^&*()'

    name = name_entry.get()
    last_name = lastname_entry.get()
    birthday = birthday_entry.get()
    age = age_entry.get()

    password_list = []
    for _ in range(10000):
        password = []
        for char in name + last_name:
            if char.isalpha():
                if char.islower():
                    password.append(random.choice(lowercase_letters))
                else:
                    password.append(random.choice(uppercase_letters))
        for char in str(age):
            password.append(random.choice(digits))
        for char in birthday:
            if char.isdigit():
                password.append(random.choice(digits))
        while len(password) < 8:
            password.append(random.choice(lowercase_letters + uppercase_letters + digits + special_chars))
        random.shuffle(password)
        password = ''.join(password)
        password_list.append(password)

    filename = "password_list.txt"
    with open(filename, 'w') as file:
        file.write('\n'.join(password_list))

    with open(filename, 'r') as file:
        passwords = file.read()

    text.delete('1.0', 'end')
    text.insert('end', passwords)

    messagebox.showinfo("Password List Generated", "Password list has been generated and saved to 'password_list.txt'")

root = tk.Tk()
root.geometry("600x540+300+70")
root.resizable(False,False)
root.iconbitmap("download.ico")
root.title("Generate a Password List App")
image1 = PhotoImage(file="images1.png")
first_frame = tk.Frame(root)
first_frame.place(x=0,y=0,width=300,height=540)

labelimage = Label(first_frame,image=image1)
labelimage.place(x=0,y=0,width=300,height=280)

text_frame = tk.Frame(root)
text_frame.place(x=300,y=0,width=300,height=550)


text = tk.Text(text_frame, padx=10, pady=10)
text.place(x=0,y=0,width=300,height=460)

# Button Frame
btn_frame = tk.Frame(root, background="white")
btn_frame.place(x=300,y=500,width=300,height=40)
def exit_function():
    root.destroy()
def open_brute_force():
    import subprocess
    root.destroy()
    subprocess.Popen(["python", "ddos.py"])
def open_bruts_ro():
    import subprocess
    subprocess.Popen(["python", "get.py"])
    
    exit_function()
    
open_brute_force_button = tk.Button(btn_frame, text="Open Brute Force", fg="white", bg="red", font=("Verdana", 11), cursor="hand2", command=open_brute_force)
open_brute_force_button.place(x=0,y=0,width=300,height=40)
get_robots = Button(root,text="Get robots",fg="white",bg="#333",font=("Verdana",10),cursor="hand2",command=open_bruts_ro)
get_robots.place(x=300,y=455,width=300,height=40)

# Labels and Entry Fields
birthday_label = tk.Label(first_frame, text="Birthday(MMDDYYYY):", fg="#222", font=("Courier", 11))
birthday_label.place(x=20, y=230)

birthday_entry = tk.Entry(first_frame)
birthday_entry.place(x=23, y=260, width=220, height=30)

namelabel = tk.Label(first_frame,text="Name:",fg="#222",font=("Courier",13))
namelabel.place(x=23,y=290)

name_entry = tk.Entry(first_frame)
name_entry.place(x=23,y=315,width=220,height=30)

lastnamelabel = tk.Label(first_frame,text="Last Name:",fg="#222",font=("Courier",13))
lastnamelabel.place(x=23,y=355)

lastname_entry = tk.Entry(first_frame)
lastname_entry.place(x=23,y=380,width=220,height=30)

labelage = tk.Label(first_frame,text="Age:",fg="#222",font=("Courier",12))
labelage.place(x=23,y=410)

age_entry = tk.Spinbox(first_frame,from_=0,to=100)
age_entry.place(x=23,y=435,width=220,height=30)

# Submit Button
submit_button = tk.Button(first_frame, text="Generate", fg="white", bg="red", font=("verdana", 13), command=generate_password_list)
submit_button.place(x=23, y=480, width=220, height=40)

root.mainloop()
