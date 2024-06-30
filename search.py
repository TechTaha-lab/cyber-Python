import tkinter
import re
from tkinter import messagebox
from tkinter import *
from tkinter import scrolledtext as sc
from tkinter import ttk
import tkinter.filedialog as fd
import whois
import requests
from bs4 import BeautifulSoup
import threading
import subprocess

import re
import random
window = Tk()
window.geometry("700x500+400+100")
window.iconbitmap("download.ico")
window.title("Get Information About Any Website")
window.resizable(False, False)

frame = Frame(window)
frame.place(x=0, y=0, width=230, height=500)
addimage = PhotoImage(file="images1.png")
labelimage = Label(frame, image=addimage)
labelimage.place(x=0, y=0, width=230, height=350)

def open_ddos():
    import time
    time.sleep(2)
    exits()
    subprocess.Popen(["python", "tests.py"])

def start_searching():
    def start_scan():
        try:
            domain = labelsph.get()
            w = whois.whois(domain)
            response = requests.get("http://" + domain)
            soup = BeautifulSoup(response.content, "html.parser")
            programming_language = soup.find("meta", attrs={"name": "generator"})
            tree.delete(*tree.get_children())

            tree.insert("", "end", values=("Domain", w.domain))
            tree.insert("", "end", values=("Registrar", w.registrar))
            tree.insert("", "end", values=("Creation Date", w.creation_date))
            tree.insert("", "end", values=("Expiration Date", w.expiration_date))
            tree.insert("", "end", values=("Name Servers", w.name_servers))
            tree.insert("", "end", values=("Programming Language", programming_language))
            print(w)
            print(response)
            print(soup)
            print(programming_language)
            if programming_language:
                programming_language = programming_language.get("content")
            else:
                programming_language = "Unknown"
                
            labelsph.delete(0, "end")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    threading.Thread(target=start_scan).start()

def exits():
    if messagebox.askquestion("question","you want to exit:"):
        window.destroy()
    else:
        window.mainloop()

buttonsframe = Frame(window)
buttonsframe.place(x=0, y=350, width=230, height=250)

btn3 = Button(window, text="OPEN DDOS", fg="white",cursor="hand2",bg="black", font=("Verdana", 10), command=open_ddos)
btn3.place(x=20, y=320, width=200, height=40)

labetitle = Label(buttonsframe, text="webn:", fg="#222", font=("Courier", 13))
labetitle.place(x=3, y=23)

labelsph = Entry(buttonsframe)
labelsph.place(x=56, y=20, width=170, height=30)

bt2 = Button(buttonsframe, text="Start Searching", fg="white", bg="royalblue", cursor="hand2", command=start_searching)
bt2.place(x=10, y=60, width=200, height=40)

bt1 = Button(buttonsframe, text="Exit", fg="white", bg="red", cursor='hand2', command=exits)
bt1.place(x=10, y=103, width=200, height=40)

tree = ttk.Treeview(window, columns=("property", "value"))
style = ttk.Style(window)
style.theme_use("clam")
style.configure('Treeview', rowheight=35, background='#d8d8d8',
                fieldbackground='#d8d8d8', foreground='black')

tree.heading("#0", text="Property", anchor=CENTER)
tree.heading("#1", text="value", anchor=CENTER)


tree.column("property", width=268)
tree.column("value", width=268)

tree.place(x=230, y=0, width=470, height=500)

taha = sc.ScrolledText(tree)

window.mainloop()
