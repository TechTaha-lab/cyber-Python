from tkinter import *
from tkinter import messagebox
import ipaddress

def calculate_network():
    try:
        ip_input = entry_ip.get()
        bits_input = int(entry_bits.get())

        network = ipaddress.IPv4Network(f"{ip_input}/{bits_input}", strict=False)

        network_address = network.network_address
        first_usable_host = network_address + 1
        last_usable_host = network.broadcast_address - 1
        broadcast_address = network.broadcast_address

        result_text = f"Network Address: {network_address}\n"
        result_text += f"First Usable Host: {first_usable_host}\n"
        result_text += f"Last Usable Host: {last_usable_host}\n"
        result_text += f"Broadcast Address: {broadcast_address}"

        text.delete(1.0, END) 
        text.insert(END, result_text)
    except ValueError as e:
        messagebox.showerror("Error","first an you have to enter an ip and number of subnets ")

window = Tk()
window.geometry("700x450+250+200")
window.resizable(False, False)
window.iconbitmap("download.ico")
window.title("Networkig app")

frame1 = Frame(window)
frame1.place(x=0, y=0, width=300, height=450)

frame2 = Frame(window)
frame2.place(x=300, y=0, width=400, height=450)

image1 = PhotoImage(file="images1.png")
label = Label(frame1, image=image1)
label.place(x=0, y=0, width=300, height=200)

label_ip = Label(window, text="IP Address:", fg="#333", font=("Courier", 11))
label_ip.place(x=10, y=220)
entry_ip = Entry(window)
entry_ip.place(x=120, y=220, width=150, height=30)

label_bits = Label(window, text="Number of Bits:", fg="#333", font=("Courier", 11))
label_bits.place(x=10, y=260)
entry_bits = Entry(window)
entry_bits.place(x=150, y=260, width=130, height=30)

btn = Button(window, text="Start", bg="#333", fg="white", font=("Courier", 11), cursor="hand2", command=calculate_network)
btn.place(x=30, y=320, width=220, height=30)
def extbutton():
    if messagebox.askokcancel("","are you sure you want to exit"):
        window.destroy()
    else:
        return
extbtn = Button(frame1,text="Exit",fg="white",bg="red",font=("Courier",12),cursor="hand2",command=extbutton)
extbtn.place(x=30,y=400,width=220,height=30)
def open():
    import subprocess
    if messagebox.askquestion("","are you sure you want to exit this app"):
        subprocess.Popen(["python","sql.py"])
        window.destroy()
    else:
        return
sqlbtn = Button(frame1,text="Get sql",fg="white",bg="royalblue",font=("Courier",12),cursor="hand2",command=open)
sqlbtn.place(x=30,y=360,width=220,height=30)
text = Text(frame2, fg="#222", padx=10, pady=10)
text.place(x=0, y=0, width=400, height=450)

window.mainloop()
