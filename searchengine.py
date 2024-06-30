import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import requests


def search_vulnerabilities():
    vulnerabilities = en2.get()
    country = en3.get()

    if vulnerabilities:
        search_url = f"https://www.google.com/search?q={vulnerabilities}{country}"
        print(search_url)
        content = requests.get(search_url)
        if content.status_code==200:
            messagebox.showinfo("","website founded")
        elif content.status_code == 404:
            messagebox.showinfo("","website does not found")
        webbrowser.open(search_url)
    else:
        messagebox.showerror("Error", "Please enter a vulnerability to search.")

def exit():
    if messagebox.askquestion("Exit", "Are you sure you want to exit?"):
        root.destroy()
    else:
        root
root = tk.Tk()
root.title("Search Engine")
root.geometry("450x400+400+200")
root.resizable(False, False)
root.iconbitmap("download.ico")

frame1 = Frame(root)
frame1.place(x=0, y=0, width=180, height=400)
imagelab = PhotoImage(file="images1.png")
lab1 = Label(frame1, image=imagelab)
lab1.place(x=0, y=0, width=180, height=150)

frame2 = Frame(root)
frame2.place(x=180, y=0, height=400, width=270)

text = Text(frame2, padx=10, pady=10, font=("Poppins", 10))
text.place(x=0, y=0, width=270, height=400)

lab2 = Label(frame1, text="Vulnerability:", fg="#333", font=("Poppins", 10))
lab2.place(x=10, y=170)

en2 = Entry(frame1)
en2.place(x=10, y=190, width=120, height=25)

lab3 = Label(frame1, text="country name:", fg="#333", font=("Poppins", 10))
lab3.place(x=10, y=220)

en3 = Entry(frame1)
en3.place(x=10, y=240, width=120, height=25)
btn1 = Button(frame1, text="Search", fg="#fff", bg="royalblue", cursor="hand2", command=search_vulnerabilities)
btn1.place(x=10, y=300, height=30, width=120)

btn2 = Button(frame1, text="Exit", fg="white", bg="red", font=("Poppins", 10), cursor="hand2", command=exit)
btn2.place(x=10, y=370, width=120, height=30)
def opens():
    root.destroy()
    import subprocess
    subprocess.Popen(["python","panel.py"])
btn3 = Button(frame1,text="panel site",fg="white",bg="#111",font=("Poppins",10),cursor="hand2",command=opens)
btn3.place(x=10,y=335,height=30,width=120)
root.mainloop()
