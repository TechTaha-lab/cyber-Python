import tkinter
import re
from tkinter import messagebox
from tkinter import *
from tkinter import scrolledtext as sc
from tkinter import ttk
import phonenumbers 
from phonenumbers import geocoder, carrier, timezone
import re
import random
import threading

window = Tk()
window.geometry("1000x500+200+100")
window.iconbitmap("download.ico")
window.title("Searching by Phone Number")
window.resizable(False, False)

frame = Frame(window)
frame.place(x=0, y=0, width=230, height=500)
addimage = PhotoImage(file="images1.png")
labelimage = Label(frame, image=addimage)
labelimage.place(x=0, y=0, width=230, height=350)
total_founded = 0
# ====================buttons frame===========================
def starts():
    number = labelsph.get()
    global total_founded
    try:
        parsed_number = phonenumbers.parse(number, None)
        
        if phonenumbers.is_valid_number(parsed_number):
            region = geocoder.description_for_number(parsed_number, "en")
            service_provider = carrier.name_for_number(parsed_number, "en")
            time_zone = timezone.time_zones_for_number(parsed_number)
            
            possible_carriers = []
            number_type = phonenumbers.phonenumberutil.number_type(parsed_number)
            if phonenumbers.PhoneNumberType.MOBILE == number_type:
                possible_carriers.append("Mobile")
            
            owner_name = "N/A"
            owner_info = phonenumbers.PhoneNumberMatcher(number, "en")
            if owner_info.has_next():
                owner_name = owner_info.next().raw_string
            
            tv.insert("", "end", values=(service_provider, time_zone, region, ", ".join(possible_carriers)))
            labelsph.delete(0, "end")
            total_founded+=1
        else:
            messagebox.showerror("Error", "Invalid phone number")
    except phonenumbers.phonenumberutil.NumberParseException:
        messagebox.showerror("Error", "You should enter a number to start searching")

def exits():
     if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        window.destroy()
     else:
        window.mainloop()

# ======================functions to start searching=======
buttonsframe = Frame(window)
buttonsframe.place(x=0, y=350, width=230, height=250)

labetitle = Label(buttonsframe, text="Phone:", fg="#222", font=("Courier", 12))
labetitle.place(x=3, y=23)

labelsph = Entry(buttonsframe)
labelsph.place(x=60, y=20, width=205, height=30)

bt2 = Button(buttonsframe, text="Start Searching", fg="white", bg="royalblue", cursor="hand2", command=starts)
bt2.place(x=10, y=60, width=200, height=40)

def openwebtesting():
    if messagebox.askokcancel("Continue", "Are you sure you want to Continue?"):
        import subprocess
        subprocess.Popen(["python","search.py"])
        exits()

b13 = Button(frame, text="Open wbscan", fg="white", bg="#222", command=openwebtesting)
b13.place(x=10, y=305, width=200, height=40)

bt1 = Button(buttonsframe, text="Exit", fg="white", bg="red", cursor='hand2', command=exits)
bt1.place(x=10, y=103, width=200, height=40)

tv = ttk.Treeview(window)
style = ttk.Style(window)
style.theme_use('clam')
style.configure('Treeview', rowheight=35, background='#d8d8d8',
                fieldbackground='#d8d8d8', foreground='black')

tv['columns'] = ('namesocial', 'urlname', 'username', 'status')
tv.column('#0', width=0, stretch=NO)  # Hide the first column
tv.column('namesocial', anchor=CENTER, width=120)
tv.column('urlname', anchor=CENTER, width=130)
tv.column('username', anchor=CENTER, width=120)
tv.column('status', anchor=CENTER, width=100)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('namesocial', text='Service Providers', anchor=CENTER)
tv.heading('urlname', text='Time Zone', anchor=CENTER)
tv.heading('username', text='Region', anchor=CENTER)
tv.heading('status', text='Owner Name', anchor=CENTER)

tv.place(x=230, y=0, width=770, height=550)

taha = sc.ScrolledText(tv)

window.mainloop()
