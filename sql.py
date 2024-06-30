import tkinter as tk
from tkinter import messagebox
import requests
import re
import threading

def scan_website():
    url = en1.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status() 

        sql_patterns = ['sql', 'select', 'union', 'from', 'where', 'and', 'or']
        content = response.text.lower()

        if any(pattern in content for pattern in sql_patterns):
            result = "This website may be vulnerable to SQL injection."
            messagebox.showinfo("warning","this website was infected in sql injection")
        else:
            result = "This website does not appear to be vulnerable to SQL injection."
            messagebox.showinfo("warning","this website was not infected in sql injection")

        textbox.delete(1.0, tk.END)
        textbox.insert(tk.END, content)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def exit_app():
    if messagebox.askquestion("", "Are you sure you want to exit?"):
        root.destroy()
    else:
        return

    subprocess.Popen(["python","panel.py"])
root = tk.Tk()
root.geometry("500x400+390+190")
root.resizable(False, False)
root.title("Website SQL Injection Scanner")
root.iconbitmap("download.ico")

frame1 = tk.Frame(root)
frame1.place(x=0, y=0, width=190, height=400)
pythonimages = tk.PhotoImage(file="images1.png")
imagelabel = tk.Label(frame1, image=pythonimages)
imagelabel.place(x=0, y=0, width=190, height=190)

frame2 = tk.Frame(root)
frame2.place(x=190, width=310, height=400)

textbox = tk.Text(frame2, padx=10, pady=10, font=("Poppins", 9))
textbox.place(x=0, y=0, width=310, height=400)

deflabel = tk.Label(frame1, text="URL:", font=("Poppins", 12), fg="#222")
deflabel.place(x=10, y=210)

en1 = tk.Entry(frame1)
en1.place(x=10, y=235, width=150, height=30)

scanbtn = tk.Button(frame1, text="Start scanning", fg="white", bg="#111", font=("Poppins", 9), cursor="hand2", command=scan_website)
scanbtn.place(x=10, y=275, width=150, height=30)
def ope():
    import subprocess
    if messagebox.showwarning("look","are you sure you want to open "):
        subprocess.Popen(["python","searchengine.py"])
        root.destroy()
    else:
        return
sbtn = tk.Button(frame1, text="search", fg="#fff", bg="#333", font=("Poppins", 9), cursor="hand2", command=ope)
sbtn.place(x=10, y=315, width=150, height=30)

exbtn = tk.Button(frame1, text="Exit", fg="#fff", bg="red", font=("Poppins", 9), cursor="hand2", command=exit_app)
exbtn.place(x=10, y=350, width=150, height=30)

root.mainloop()
