import tkinter as tk
from tkinter import scrolledtext
import nmap
from threading import Thread
from tkinter import messagebox
def exit_function():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()
    else:
        root.mainloop()

def get_port_function():
    target = entry_target.get()
    if target.startswith("https://") or target.startswith("http://"):
        messagebox.showerror("Error","there is an error")   
    if target:
        nm = nmap.PortScanner()
        result = nm.scan(target, arguments="-p1-65535")
        
        text_area.delete(1.0, tk.END)  
        for port in result['scan'][target]['tcp']:
            state = result['scan'][target]['tcp'][80]['state']
            print(state)
    else:
        text_area.insert(tk.END, "Please enter a target")

root = tk.Tk()
root.geometry("600x300+400+100")
root.iconbitmap("downloads_icons.ico")
root.resizable(False, False)
root.title("Get Open and Closed Ports")

frame1 = tk.Frame(root, background="#fff")
frame1.place(x=0, y=0, width=250, height=300)

image1 = tk.PhotoImage(file="images1.png")

label_image = tk.Label(frame1, image=image1)
label_image.place(x=0, y=0, width=250, height=300)

frame2 = tk.Frame(root, background="whitesmoke", relief=tk.RIDGE)
frame2.place(x=250, y=0, width=350, height=150)

label_name = tk.Label(frame2, text="Enter a target:", fg="#333", bg="whitesmoke", font=("Verdana", 11))
label_name.place(x=20, y=20)

entry_target = tk.Entry(frame2, bd=8, insertwidth=2, font=('arial', 9, 'bold'), borderwidth=2)
entry_target.place(x=22, y=50, width=200, height=40)

btn_exit = tk.Button(frame2,text="Exit", fg="white", bg="red", font=("Verdana", 11), borderwidth=2,
                     cursor="hand2", command=exit_function)
btn_exit.place(x=22, y=100, width=175, height=40)

btn_get_port = tk.Button(frame2, text="Get Port", fg="white", bg="royalblue", font=("Arial", 10), cursor="hand2",
                         command=get_port_function)
btn_get_port.place(x=175, y=100, width=150, height=40)

btn_frame = tk.Frame(root, background="white", relief=tk.RIDGE)
btn_frame.place(x=250, y=150, width=350, height=150)

text_area = scrolledtext.ScrolledText(btn_frame, padx=10, pady=10)
text_area.place(x=0, y=0, width=350, height=150)

root.mainloop()
