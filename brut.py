# import random
# data_list ="abcdefgchigklmnopqrstuvxyz0123456789"
# chardata = list(data_list)
# password = str(input("enter a password here:"))
# myguess = ""
# while(myguess != password):
#     myguess = random.choices(chardata,k=len(password))
#     print(myguess)
#     myguess="".join(myguess)
# print("your password is:"+myguess)from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox
from tkinter import *
def validate_input():
    entry_text = entry.get()
    selected_type = type_var.get()

    if selected_type == "Website":
        if is_website(entry_text):
            messagebox.showinfo("Valid Input", "Website: " + entry_text)
        else:
            messagebox.showerror("Invalid Input", "Invalid website format")
    elif selected_type == "Account":
        if is_account(entry_text):
            messagebox.showinfo("Valid Input", "Account: " + entry_text)
        else:
            messagebox.showerror("Invalid Input", "Invalid account format")
    else:
        messagebox.showerror("Invalid Selection", "Please select an input type")

def is_website(entry):
    website_pattern = r"^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/?$"
    return re.match(website_pattern, entry) is not None

def is_account(entry):
    account_pattern = r"^[a-zA-Z0-9_]{3,}$"
    return re.match(account_pattern, entry) is not None

root = Tk()

type_var = StringVar()
type_var.set("Website")
type_menu = OptionMenu(root, type_var, "Website", "Account")
type_menu.pack()

entry = Entry(root)
entry.pack()

submit_btn = Button(root, text="Submit", command=validate_input)
submit_btn.pack()

root.mainloop()
