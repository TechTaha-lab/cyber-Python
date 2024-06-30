import subprocess
import tkinter as tk
from tkinter import messagebox
import pyttsx3
taha = pyttsx3.init()

def exitbutton():
    import pyttsx3
    t = pyttsx3.init()
    textp = "are you sure you want to exit"
    print(textp)
    t.say(textp)
    t.runAndWait()
    if messagebox.askokcancel("","are you sure you want to exit"):
        root.destroy()
    else:
        return
def get_connected_devices():
    text.delete(1.0, tk.END)
    ip_address = en1.get()
    interface = en2.get()

    if not ip_address or not interface:
        errormessage = "please enter an ip address and interface name"
        taha.say(errormessage)
        taha.runAndWait()
        messagebox.showerror("error","please enter an ip address and an interface name")
        return

    try:
        result = subprocess.check_output(["arp", "-n", "-i", interface])
        result = result.decode("utf-8")
        lines = result.split("\n")

        connected_devices = set()
        for line in lines:
            if ip_address in line:
                parts = line.split()
                if len(parts) >= 3:
                    connected_devices.add(parts[0])

        if not connected_devices:
            textmessage = "no device are found on the network please try again!!"
            taha.say(textmessage)
            taha.runAndWait()
            messagebox.showerror("error","no devices are found on the network")
        else:
            text.insert(tk.END, "Connected devices:\n")
            for device in connected_devices:
                text.insert(tk.END, device + "\n")

    except Exception as e:
        errormessages = "there is an error here please try again!"
        taha.say(errormessages)
        taha.runAndWait()
        

root = tk.Tk()
root.geometry("700x440+260+170")
root.resizable(False, False)
root.iconbitmap("download.ico")
root.title("Python software to get the IP connected with WiFi")

frame1 = tk.Frame(root)
frame1.place(x=0, y=0, width=300, height=440)

img1 = tk.PhotoImage(file="images1.png")
label = tk.Label(frame1, image=img1)
label.place(x=0, y=0, width=300, height=200)

label1 = tk.Label(frame1, text="IP Address:", fg="#222", font=("Courier", 14))
label1.place(x=10, y=210)

en1 = tk.Entry(frame1, fg="#222")
en1.place(x=15, y=240, width=200, height=30)

label2 = tk.Label(frame1, text="Interface Name:", fg="#222", font=("Courier", 13))
label2.place(x=15, y=280)

en2 = tk.Entry(frame1)
en2.place(x=15, y=310, height=30, width=200)

button1 = tk.Button(frame1, text="Start", fg="white", bg="#333", font=("Courier", 12), cursor="hand2", command=get_connected_devices)
button1.place(x=20, y=350, height=30, width=200)

frame2 = tk.Frame(root)
frame2.place(x=300, height=440, width=400, y=0)

button2 = tk.Button(frame1, text="Exit", fg="white", bg="red", font=("Courier", 12), cursor="hand2", command=exitbutton)
button2.place(x=20, y=410, height=30, width=200)
def openip():
    import subprocess
    root.destroy()
    subprocess.Popen(["python","subnetmask.py"])
    taha.say("the file has been opened")
    taha.runAndWait()

button3 = tk.Button(frame1, text="open ips", fg="white", bg="royalblue", font=("Courier", 12), cursor="hand2", command=openip)
button3.place(x=20, y=380, height=30, width=200)

text = tk.Text(frame2, padx=10, pady=10)
text.place(x=0, y=0, height=440, width=400)

root.mainloop()
