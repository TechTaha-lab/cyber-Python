import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import string
import requests
import threading

root = tk.Tk()
root.title("Find Admin Panel for Site")
root.iconbitmap("download.ico")
root.geometry("550x390+370+100")
root.resizable(False, False)

# start dividing the app into frames
frame1 = Frame(root)
frame1.place(x=0, y=0, width=200, height=420)

frame2 = Frame(root)
frame2.place(x=205, y=0, width=345, height=390)
textarea = Text(frame2)
textarea.place(x=0, y=0, width=345, height=390)

img_label = PhotoImage(file="images1.png")
labimages = Label(frame1, image=img_label)
labimages.place(x=0, y=0, width=200, height=200)

urllabel = Label(frame1, text="URL site:", fg="#333", font=("Courier", 10))
urllabel.place(x=10, y=210)
en1 = Entry(frame1, foreground="#222", fg="#222", font=("Poppins", 10))
en1.place(x=84, width=120, height=24, y=210)

def generate_admin_words():
    url = en1.get()
    admin_words = [f"{word}.php" for word in generate_random_words()]

    with open(f"{url}_admin_words.txt", "w") as file:
        file.write("\n".join(admin_words))

    messagebox.showinfo("Admin Words Generated", "Admin words have been generated and saved to a file.")

def generate_random_words():
    word_list = []
    for _ in range(100000):
        word = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        word_list.append(word)
    return word_list

def start_brutting():
    def brute_force():
        target = en1.get()
        try:
            f=open("_admin_words.txt","r")
            file = f.read()
            pages = file.splitlines()

            for x in pages:
                domain = target + x
                try:
                    req = requests.get(domain)
                    if req.status_code == 200:
                        textarea.insert(tk.END, "[+] page not found: " + '/'+ domain +  "\n")
                    else:
                        textarea.insert(tk.END, "[-] page found: " + '/'+ domain + "\n")
                except requests.exceptions.RequestException:
                    textarea.insert(tk.END, "[-] Unable to connect to: " + domain + "\n")
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "Admin word file not found. Please generate admin words first.")
    
    thread = threading.Thread(target=brute_force)
    thread.start()

startbutton = Button(frame1, text="ATTACK", fg="#fff", bg="#111", font=("Poppins", 10), cursor="hand2", command=start_brutting)
startbutton.place(x=10, y=250, width=200, height=30)

generatebuttons = Button(frame1, text="Generate", fg="#111", bg="silver", font=("Poppins", 10), cursor="hand2", command=generate_admin_words)
generatebuttons.place(x=10, y=285, width=200, height=30)

def exitbutton():
    if messagebox.askokcancel('Exit', "Do you want to exit?"):
        root.destroy()

exitbtn = Button(frame1, text="Exit", fg="#fff", bg="red", cursor="hand2", font=("Courier", 10), command=exitbutton)
exitbtn.place(x=10, y=325, height=30, width=200)

root.mainloop()
