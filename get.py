from tkinter import *
import tkinter.messagebox as messagebox
import requests
from bs4 import BeautifulSoup
import tkinter as tk

def quit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()
        print("The program has been destroyed.")
    else:
        print("Hello")

def delete_textarea_data():
    text1.delete("1.0", tk.END)

def save_data_scraped():
    data = text1.get("1.0", tk.END)
    
    if data.strip() == "":
        messagebox.showerror("Error", "The textarea is empty. Start scraping.")
    else:
        try:
            with open("taha.txt", "w", encoding="utf-8") as file:
                file.write(data)
        except Exception as e:
            print("Failed to create a file:", e)
        messagebox.showinfo("Success", "Data saved successfully")

def get_robots():
     url = entry.get()

     if url.startswith("https://") or url.startswith("http://"):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        divfinds = soup.find_all("div")

        for div in divfinds:
            title_element = div.find("h2")
            if title_element:
                title_name = title_element.text.strip()
                print(title_name.encode('utf-8', errors='ignore').decode())  # Encode and decode to handle special characters

        soup_text = soup.prettify()
        text1.delete("1.0", "end")

        taha1 = entry1.get()
        taha2 = entrylabel1.get()
        taha3 = entrylabel2.get()

        if taha2 != "":
            find_with_divs_id = soup.find_all(taha1, id=taha2)
            text1.insert("end", find_with_divs_id)
        else:
            messagebox.showerror("Error", "Try to fill in the input.")

        if taha3 != "":
            find_with_divs_class = soup.find_all(taha1, class_=taha3)
            text1.insert("end", find_with_divs_class)
        else:
            messagebox.showerror("Error", "There is an error.")

        finds_all = soup.find_all(taha1)
        text1.insert("end", finds_all)
     else:
        messagebox.showerror("Error", "Please enter a website URL in the format: https://www.example.com")
    
root = Tk()
root.geometry("700x500+250+100")
root.title("Get Web Robots File")
root.iconbitmap("downloads_icons.ico")
root.configure(background="whitesmoke")
root.resizable(False,False)
frame1 = Frame(root, background="whitesmoke")
frame1.place(x=0, y=0, width=300, height=400)

images1 = PhotoImage(file="images1.png")
label1 = Label(frame1, image=images1)
label1.place(x=0, y=0, width=300, height=220)

labelname = Label(frame1, text="Target URL:", fg="#333", bg="whitesmoke", padx=5, pady=5, font=("Verdana", 10))
labelname.place(x=10, y=225)

entry = Entry(frame1, borderwidth=1, insertwidth=2)
entry.place(x=20, y=260, width=220, height=40)

labelnamea = Label(frame1, text="Scrape by TagName:", fg="#333", bg="whitesmoke", padx=5, pady=5, font=("Verdana", 10))
labelnamea.place(x=10, y=300)

entryframe = Frame(root, background="whitesmoke")
entryframe.place(x=300, y=350, width=400, height=150)

entry1 = Entry(frame1, borderwidth=1, insertwidth=1)
entry1.place(x=20, y=335, width=220, height=40)

btnframe = Frame(root, background="whitesmoke")
btnframe.place(x=0, y=380, width=300, height=100)

labelentry1 = Label(entryframe, text="Enter the Id(Optional):", fg="#333", bg="whitesmoke", padx=10, pady=10, font=("Verdana", 10))
labelentry1.place(x=0, y=0)

entrylabel1 = Entry(entryframe, borderwidth=1, insertwidth=1)
entrylabel1.place(x=10, y=40, width=200, height=30)

labelentry2 = Label(entryframe, text="Enter a class(Optional):", fg="#333", bg="whitesmoke", font=("Verdana", 10))
labelentry2.place(x=10, y=72)

entrylabel2 = Entry(entryframe, borderwidth=1, insertbackground="#333", insertwidth=1)
entrylabel2.place(x=10, y=100, width=200, height=30)

btn1 = Button(btnframe, text="Get robots", fg="#fff", bg="royalblue", font=("Verdana", 10), cursor="hand2", command=get_robots)
btn1.place(x=20, y=15, width=250, height=40)

btn2 = Button(btnframe, text="Exit", fg="#fff", bg="red", font=("Verdana", 10), cursor="hand2", command=quit_program)
btn2.place(x=20, y=60, width=250, height=40)

text1 = Text(root)
text1.place(x=300, y=0, width=400, height=350)

deletebtn = Button(entryframe, text="Delete", fg="white", bg="red", font=("Verdana", 10), cursor="hand2", command=delete_textarea_data)
deletebtn.place(x=250, y=40, width=100, height=30)

savebtn = Button(entryframe, text="Save As", fg="white", bg="#222", font=("Verdana", 10), cursor="hand2", command=save_data_scraped)
savebtn.place(x=250, y=105, width=100, height=30)

root.mainloop()
