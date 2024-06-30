import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title('email and phone scraper')
root.resizable(False,False)
root.geometry('500x340+400+200')
root.iconbitmap('download.ico')
# now we start to add a some function
def data_scraper():
    entrys = en1.get()
    if len(entrys) == 0:
        messagebox.showerror('empty','please enter a url here')
    elif entrys.startswith('https') or entrys.startswith('http'):
        from scrapify import Scraper
        url = entrys
        scraper = Scraper(url)
        phone_number = scraper.find('<span class="phone"></span>')
        linked_email = scraper.find('<span class="email"></span>')
        if(phone_number and linked_email):
            messagebox.showinfo('success',f'phone number and email are founded:${phone_number}${linked_email}')
            t1.insert(0,tk.END,phone_number)
            t1.insert(0,tk.END,linked_email)
            
        else:
            messagebox.showerror('not found','phone and email are not found')
    else:
        messagebox.showerror('error','invalid site format')
    
def exit_function():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()
    else:
        return root

# now we start divide our app into frames and we pyt inside the frames some content and information needed
f1 = tk.Frame(root,background="white")
f1.place(x=0,y=0,width=240,height=340)
# now we start put some content inside the firts frame

im1 = tk.PhotoImage(file='images1.png')
l1 = tk.Label(f1,image=im1,background='white')
l1.place(x=10,y=30,width=230,height=130)

# now starting to add a input 
l2 = tk.Label(f1,text='website Name:',fg='#222',bg='white',font=('Courier',11))
l2.place(x=10,y=170)

en1 = tk.Entry(f1)
en1.place(x=10,y=195,width=200,height=30)

#===now start add the buttons===
b1 = tk.Button(f1,text="start",fg="white",bg="#222",font=('Courier',11),cursor='hand2',command=data_scraper)
b1.place(x=10,y=255,width=200,height=35)


b2 = tk.Button(f1,text="Exit",fg="white",bg="red",font=('Courier',11),cursor='hand2',command=exit_function)
b2.place(x=10,y=295,width=200,height=35)



# ===== add a texarea inside the frame2  ============
f2 = tk.Frame(root)
f2.place(x=240,y=0,height=340,width=260)

t1 = tk.Text(f2,padx=10,pady=10)
t1.place(x=0,y=0,width=260,height=340)
root.mainloop()