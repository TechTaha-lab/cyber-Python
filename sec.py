from tkinter import *
import tkinter.scrolledtext as sc
import threading
from bs4 import BeautifulSoup as bc
from tkinter import ttk
import requests
import tkinter.font as taha
from openpyxl import *
import pandas as pd
import time
root = Tk()
root.geometry('970x560+200+100')
root.title("taha cherlock")
root.iconbitmap("downloads_icons.ico")
root.configure(background='whitesmoke')
# root.iconbitmap('download.ico')
root.resizable(False, FALSE)
total_founded = 0
# ============================================
logoimages = PhotoImage(file="download_icons_1.png")
title = Label(root, text='Cyber Security Tools',
              font=('Verdana', 14), bg='whitesmoke', fg='#333')
title.pack(fill=X)
photo = PhotoImage(file='download.png')
photos = PhotoImage(file='images1.png')

panel1 = Label(root, image=photos)
panel1.place(x=2, y=35, width='200', height='440')
l1 = Label(root, text='USER:')
l1.place(x=5, y=360)
en1 = Entry(root, font=('Arial', '12'), justify=CENTER)
en1.place(x=40, y=360, width=150, height=24)
exitimages = PhotoImage(file="R.png",width=184,height=40)

style = ttk.Style()
font_awesome = taha.Font(family="Font Awesome 5 Free", size=12)  

style.configure("Custom.TButton")
def go():
    def save_to_excel():
        data = []
        for item in tv.get_children():
                 values = []
        for column in tv.item(item)['values']:
            values.append(column)
        data.append(values)
    
    if data:
        df = pd.DataFrame(data, columns=["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"])
        df.to_excel("informa.xlsx", index=False)
        print("Data saved to data.xlsx")
    else:
        print("No data in Treeview.")
    save_to_excel()
    threading.Thread(target=data).start()


def data():
    username = en1.get()
    def savedata():
        searches = en1.get()
        from openpyxl import Workbook
        workbook = Workbook() 
        sheets = workbook.active
        sheets.append([searches])
        workbook.save('datainformations.xlsx')
    def savetreviewdata():
        import pandas as pd
        data = []
        columns = []
    

    savedata()
    def face():
        global total_founded
        facebook_url = 'https://www.facebook.com/'
        r = requests.get(facebook_url+username)
        soup = bc(r.content, 'html.parser')
        title1 = soup.find('title')
        a1 = title.__str__
        if a1 == 'facebook':
            text1.insert('end', '[+]facebook:', 'blue')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', facebook_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="facebook acc", index=0, values=(
                'facebook', facebook_url, username, 'FOUND'))
            total_founded += 1

    def instagram():
        global total_founded
        insta_url = 'https://www.instagram.com/'
        r = requests.get(insta_url+username)
        soup = bc(r.content, 'html.parser')
        title2 = soup.find('title')
        a1 = title.__str__
        if a1 == 'instagram':
            text1.insert('end', '[+]instagram:', 'pink')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', insta_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="instagram acc", index=0, values=(
                'instagram', insta_url, username, 'FOUND'))
            total_founded +=1

    def github():
        global total_founded
        github_url = 'https://www.github.com/'
        r = requests.get(github_url+username)
        soup = bc(r.content, 'html.parser')
        title3 = soup.find('title')
        a1 = title.__str__
        if a1 == 'github':
            text1.insert('end', '[+]github:', 'blue')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', github_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="github acc", index=0, values=(
                'github', github_url, username, 'FOUND'))
        total_founded += 1
    def snapchat():
        global total_founded
        snap_url = 'https://www.snapchat.com/'
        r = requests.get(snap_url+username)
        soup = bc(r.content, 'html.parser')
        title4 = soup.find('title')
        a1 = title.__str__
        if a1 == 'snapchat':
            text1.insert('end', '[+]snapchat:', 'yellow')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', snap_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="snapchat acc", index=0, values=(
                'snapchat', snap_url, username, 'FOUND'))
            total_founded+=1

    def google():
        global total_founded
        google_url = 'https://www.google.com/'
        r = requests.get(google_url+username)
        soup = bc(r.content, 'html.parser')
        title5 = soup.find('title')
        a1 = title.__str__
        if a1 == 'google':
            text1.insert('end', '[+]google:', 'red')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', google_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="google acc", index=0, values=(
                'google', google_url, username, 'FOUND'))
            total_founded += 1

    def youtube():
        global total_founded
        youtube_url = 'https://www.youtube.com/'
        r = requests.get(youtube_url+username)
        soup = bc(r.content, 'html.parser')
        title6 = soup.find('title')
        a1 = title.__str__
        if a1 == 'youtube':
            text1.insert('end', '[+]youtube:', 'red')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', youtube_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="youtube acc", index=0, values=(
                'youtube', youtube_url, username, 'FOUND'))
        total_founded += 1
    def amazon():
        global total_founded
        amazon_url = 'https://www.amazon.com/'
        r = requests.get(amazon_url+username)
        soup = bc(r.content, 'html.parser')
        title7 = soup.find('title')
        a1 = title.__str__
        if a1 == 'amazon':
            text1.insert('end', '[+]amazon:', '#333')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', amazon_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="amazon acc", index=0, values=(
                'amazon', amazon_url, username, 'FOUND'))
            total_founded += 1
    def netflix():
        global total_founded
        netflix_url = 'https://www.netflix.com/'
        r = requests.get(netflix_url+username)
        soup = bc(r.content, 'html.parser')
        title8 = soup.find('title')
        a1 = title.__str__
        if a1 == 'Netflix':
            text1.insert('end', '[+]Netflix:', '#333')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', netflix_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="Netflix acc", index=0, values=(
                'Netflix', netflix_url, username, 'FOUND'))
            total_founded+=1
    def linkedin():
        global total_founded
        linkedin_url = 'https://www.linkedin.com/'
        r = requests.get(linkedin_url+username)
        soup = bc(r.content, 'html.parser')
        title9 = soup.find('title')
        a1 = title.__str__
        if a1 == 'LinkedIn':
            text1.insert('end', '[+]LinkedIn:', '#333')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', linkedin_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="linkedin acc", index=0, values=(
                'LinkedIn', linkedin_url, username, 'FOUND'))
            total_founded +=1
    def twitter():
        global total_founded
        twitter_url = 'https://www.twitter.com/'
        r = requests.get(twitter_url+username)
        soup = bc(r.content, 'html.parser')
        title10 = soup.find('title')
        a1 = title.__str__
        if a1 == 'twitter':
            text1.insert('end', '[+]twitter:', '#333')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', twitter_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="twitter acc", index=0, values=(
                'twitter', twitter_url, username, 'FOUND'))
            total_founded += 1
    def fiverr():
        global total_founded
        fiverr_url = 'https://www.fiverr.com/'
        r = requests.get(fiverr_url+username)
        soup = bc(r.content, 'html.parser')
        title11 = soup.find('title')
        a1 = title.__str__
        if a1 == 'fiverr':
            text1.insert('end', '[+]fiverr:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', fiverr_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="fiverr acc", index=0, values=(
                'fiverr', fiverr_url, username, 'FOUND'))
            total_founded+=1
    def chatgpt():
        global total_founded 
        chat_url = 'https://chat.openai.com/'
        r = requests.get(chat_url+username)
        soup = bc(r.content, 'html.parser')
        title12 = soup.find('title')
        a1 = title.__str__
        if a1 == 'chatgpt':
            text1.insert('end', '[+]chatgpt:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', chat_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="chatgpt acc", index=0, values=(
                'chatgpt', chat_url, username, 'FOUND'))
            total_founded +=1
    def reddit():
        global total_founded
        reddit_url = 'https://www.reddit.com/'
        r = requests.get(reddit_url+username)
        soup = bc(r.content, 'html.parser')
        title12 = soup.find('title')
        a1 = title.__str__
        if a1 == 'reddit':
            text1.insert('end', '[+]reddit:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', reddit_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="reddit acc", index=0, values=(
                'reddit', reddit_url, username, 'FOUND'))
            total_founded+=1
    def pinterest():
        global total_founded
        pinterest_url = 'https://www.pinterest.com/'
        r = requests.get(pinterest_url+username)
        soup = bc(r.content, 'html.parser')
        title13 = soup.find('title')
        a1 = title.__str__
        if a1 == 'pinterest':
            text1.insert('end', '[+]pinterest:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', pinterest_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="pinterest acc", index=0, values=(
                'pinterest', pinterest_url, username, 'FOUND'))
            total_founded+=1
    def canva():
        global total_founded
        canva_url = 'https://www.canva.com/'
        r = requests.get(canva_url+username)
        soup = bc(r.content, 'html.parser')
        title14 = soup.find('title')
        a1 = title.__str__
        if a1 == 'canva':
            text1.insert('end', '[+]canva:', 'royalblue')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', canva_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            
            tv.insert(parent='', text="canva acc", index=0, values=(
                'canva', canva_url, username, 'FOUND'))
            total_founded += 1
    # ====================finding all account of all design website===============

    def pinterest():
        global total_founded
        pinterst_url = 'https://www.pinterest.com/'
        r = requests.get(pinterst_url+username)
        soup = bc(r.content, 'html.parser')
        title13 = soup.find('title')
        a1 = title.__str__
        if a1 == 'pinterest':
            text1.insert('end', '[+]pinterest:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', pinterst_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="pinterest acc", index=0, values=(
                'pinterest', pinterst_url, username, 'FOUND'))
            total_founded += 1
    def designevo():
        global total_founded
        designevo_url = 'https://www.designevo.com/'
        r = requests.get(designevo_url+username)
        soup = bc(r.content, 'html.parser')
        title14 = soup.find('title')
        a1 = title.__str__
        if a1 == 'desginevo':
            text1.insert('end', '[+]desginevo:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', designevo_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="designevo acc", index=0, values=(
                'designevo', designevo_url, username, 'FOUND'))
            total_founded += 1
    def logojoy():
        global total_founded
        logojoy_url = 'https://www.logojoy.com/'
        r = requests.get(logojoy_url+username)
        soup = bc(r.content, 'html.parser')
        title15 = soup.find('title')
        a1 = title.__str__
        if a1 == 'logojoy':
            text1.insert('end', '[+]pinterest:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', logojoy_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="logojoy acc", index=0, values=(
                'pinterest', logojoy_url, username, 'FOUND'))
            total_founded+=1
    def tinkercad():
        global total_founded
        tinker_url = 'https://www.tinkercad.com/'
        r = requests.get(tinker_url+username)
        soup = bc(r.content, 'html.parser')
        title15 = soup.find('title')
        a1 = title.__str__
        if a1 == 'tinkercad':
            text1.insert('end', '[+]tinkercad:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', tinker_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="tinkercad acc", index=0, values=(
                'tinkercad', tinker_url, username, 'FOUND'))
            total_founded+=1
    def freelancer():
        global total_founded
        freelancer_url = 'https://www.freelancer.com/'
        r = requests.get(freelancer_url+username)
        soup = bc(r.content, 'html.parser')
        title16 = soup.find('title')
        a1 = title.__str__
        if a1 == 'freelancer':
            text1.insert('end', '[+]freelancer:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', freelancer_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="freelancer acc", index=0, values=(
                'freelancer', freelancer_url, username, 'FOUND'))
            total_founded+=1
    def tesla():
        global total_founded
        tesla_url = 'https://www.tesla.com/'
        r = requests.get(tesla_url+username)
        soup = bc(r.content, 'html.parser')
        title17 = soup.find('title')
        a1 = title.__str__
        if a1 == 'tesla':
            text1.insert('end', '[+]tesla:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', tesla_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="tesla acc", index=0, values=(
                'tesla', tesla_url, username, 'FOUND'))
            total_founded +=1
    def spacex():
        global total_founded
        spacex_url = 'https://www.spacex.com/'
        r = requests.get(spacex_url+username)
        soup = bc(r.content, 'html.parser')
        title17 = soup.find('title')
        a1 = title.__str__
        if a1 == 'space x ':
            text1.insert('end', '[+]space x:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', spacex_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="spacex acc", index=0, values=(
                'space ', spacex_url, username, 'FOUND'))
            total_founded+=1
    def twicth():
        global total_founded
        twitch_url = 'https://www.twitch.tv/'
        r = requests.get(twitch_url+username)
        soup = bc(r.content, 'html.parser')
        title18 = soup.find('title')
        a1 = title.__str__
        if a1 == 'twitch tv':
            text1.insert('end', '[+]twitch tv :', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', twitch_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="twitch acc", index=0, values=(
                'twitch ', twitch_url, username, 'FOUND'))
            total_founded +=1
    def dropbox():
        global total_founded
        dropbox_url = 'https://www.dropbox.com/'
        r = requests.get(dropbox_url+username)
        soup = bc(r.content, 'html.parser')
        title19 = soup.find('title')
        a1 = title.__str__
        if a1 == 'twitch tv':
            text1.insert('end', '[+]twitch tv :', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', dropbox_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="twitch acc", index=0, values=(
                'twitch ', dropbox_url, username, 'FOUND'))
            total_founded+=1
    def discord():
        global total_founded
        discord_url = 'https://www.discord.com/'
        r = requests.get(discord_url+username)
        soup = bc(r.content, 'html.parser')
        title20 = soup.find('title')
        a1 = title.__str__
        if a1 == 'discord':
            text1.insert('end', '[+]discord:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', discord_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="discord acc", index=0, values=(
                'discord', discord_url, username, 'FOUND'))
            total_founded+=1
    def liu():
        global total_founded
        liu_url = 'https://www.liu.edu.lb/'
        r = requests.get(liu_url+username)
        soup = bc(r.content, 'html.parser')
        title21 = soup.find('title')
        a1 = title.__str__
        if a1 == 'liu':
            text1.insert('end', '[+]liu:', 'dodgerblue')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', liu_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="liu acc", index=0, values=(
                'liu ', liu_url, username, 'FOUND'))
            total_founded+=1
    def jinan():
        global total_founded
        jinan_url = 'https://www.jinan.edu.lb/'
        r = requests.get(jinan_url+username)
        soup = bc(r.content, 'html.parser')
        title22 = soup.find('title')
        a1 = title.__str__
        if a1 == 'jinan':
            text1.insert('end', '[+]jinane:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', jinan_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="jinan acc", index=0, values=(
                'jinan', jinan_url, username, 'FOUND'))
            total_founded+=1
    def aub():
        global total_founded
        aub_url = 'https://www.aub.edu.lb/'
        r = requests.get(aub_url+username)
        soup = bc(r.content, 'html.parser')
        title23 = soup.find('title')
        a1 = title.__str__
        if a1 == 'aub':
            text1.insert('end', '[+]aub:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', aub_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="aub acc", index=0, values=(
                'aub', aub_url, username, 'FOUND'))
            total_founded+=1

    def aut():
        global total_founded
        aut_url = 'https://www.aut.edu.lb/'
        r = requests.get(aut_url+username)
        soup = bc(r.content, 'html.parser')
        title24 = soup.find('title')
        a1 = title.__str__
        if a1 == 'aut':
            text1.insert('end', '[+]aut:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', aut_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="aut acc", index=0, values=(
                'aut', aut_url, username, 'FOUND'))
            total_founded+=1

    def balamand():
        global total_founded
        balamand_url = 'https://www.balamand.edu.lb/'
        r = requests.get(balamand_url+username)
        soup = bc(r.content, 'html.parser')
        title25 = soup.find('title')
        a1 = title.__str__
        if a1 == 'balamand':
            text1.insert('end', '[+]balamand:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', balamand_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="balamand acc", index=0, values=(
                'balamand', balamand_url, username, 'FOUND'))
            total_founded+=1
    def ul():
        global total_founded 
        ul_url = 'https://www.ul.edu.lb/'
        r = requests.get(ul_url+username)
        soup = bc(r.content, 'html.parser')
        title25 = soup.find('title')
        a1 = title.__str__
        if a1 == 'lebanon uni':
            text1.insert('end', '[+]ul:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', ul_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="ul acc", index=0, values=(
                'ul', ul_url, username, 'FOUND'))
            total_founded+=1

    def bau():
        global total_founded
        bau_url = 'https://www.bau.edu.lb/'
        r = requests.get(bau_url+username)
        soup = bc(r.content, 'html.parser')
        title26 = soup.find('title')
        a1 = title.__str__
        if a1 == 'bau ':
            text1.insert('end', '[+]bau:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', bau_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="bau acc", index=0, values=(
                'bau', bau_url, username, 'FOUND'))
            total_founded+=1

    def mtv():
        global total_founded
        mtv_url = 'https://www.mtv.com.lb/'
        r = requests.get(mtv_url+username)
        soup = bc(r.content, 'html.parser')
        title27 = soup.find('title')
        a1 = title.__str__
        if a1 == 'mtv ':
            text1.insert('end', '[+]mtv:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', mtv_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="mtv acc", index=0, values=(
                'mtv', mtv_url, username, 'FOUND'))
            total_founded+=1

    def aljadeed():
        global total_founded 
        aljadeed_url = 'https://www.aljadeed.tv/'
        r = requests.get(aljadeed_url+username)
        soup = bc(r.content, 'html.parser')
        title28 = soup.find('title')
        a1 = title.__str__
        if a1 == 'aljadeed':
            text1.insert('end', '[+]aljadeed:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', aljadeed_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="aljadeed acc", index=0, values=(
                'aljadeed', aljadeed_url, username, 'FOUND'))
            total_founded+=1

    def amut():
        global total_founded
        amut_url = 'https://www.amut.edu.lb/'
        r = requests.get(amut_url+username)
        soup = bc(r.content, 'html.parser')
        title29 = soup.find('title')
        a1 = title.__str__
        if a1 == 'amut':
            text1.insert('end', '[+]amut:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', amut_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="amut acc", index=0, values=(
                'amut', amut_url, username, 'FOUND'))
            total_founded+=1

    def usj():
        global total_founded
        usj_url = 'https://www.usj.edu.lb/'
        r = requests.get(usj_url+username)
        soup = bc(r.content, 'html.parser')
        title30 = soup.find('title')
        a1 = title.__str__
        if a1 == 'amut':
            text1.insert('end', '[+]amut:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', usj_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="usj acc", index=0, values=(
                'usj ', usj_url, username, 'FOUND'))
            total_founded+=1

    def mubs():
        global total_founded
        mubs_url = 'https://www.mubs.edu.lb/'
        r = requests.get(mubs_url+username)
        soup = bc(r.content, 'html.parser')
        title31 = soup.find('title')
        a1 = title.__str__
        if a1 == 'mubs':
            text1.insert('end', '[+]mubs:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', mubs_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="mubs acc", index=0, values=(
                'mubs ', mubs_url, username, 'FOUND'))
            total_founded+=1

    def ua():
        global total_founded
        ua_url = 'https://www.ua.edu.lb/'
        r = requests.get(ua_url+username)
        soup = bc(r.content, 'html.parser')
        title32 = soup.find('title')
        a1 = title.__str__
        if a1 == 'ua':
            text1.insert('end', '[+]ua:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', ua_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="ua acc", index=0, values=(
                'ua', ua_url, username, 'FOUND'))
            total_founded+=1

    def ndu():
        global total_founded
        ndu_url = 'https://www.ndu.edu.lb/'
        r = requests.get(ndu_url+username)
        soup = bc(r.content, 'html.parser')
        title32 = soup.find('title')
        a1 = title.__str__
        if a1 == 'ndu':
            text1.insert('end', '[+]ndu:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', ndu_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="ndu acc", index=0, values=(
                'ndu', ndu_url, username, 'FOUND'))
            total_founded+=1

    def tiktok():
        global total_founded
        tiktok_url = 'https://www.tiktok.com/'
        r = requests.get(tiktok_url+username)
        soup = bc(r.content, 'html.parser')
        title33 = soup.find('title')
        a1 = title.__str__
        if a1 == 'tiktok':
            text1.insert('end', '[+]tiktok:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', tiktok_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="tiktok acc", index=0, values=(
                'tiktok', tiktok_url, username, 'FOUND'))
            total_founded+=1
    def ebay():
        global total_founded
        ebay_url = 'https://www.ebay.com/'
        r = requests.get(ebay_url+username)
        soup = bc(r.content, 'html.parser')
        title34 = soup.find('title')
        a1 = title.__str__
        if a1 == 'ebay':
            text1.insert('end', '[+]ebay:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', ebay_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="ebay acc", index=0, values=(
                'ebay', ebay_url, username, 'FOUND'))
            total_founded+=1

    def spotify():
        global total_founded
        spotify_url = 'https://www.spotify.com/'
        r = requests.get(spotify_url+username)
        soup = bc(r.content, 'html.parser')
        title35 = soup.find('title')
        a1 = title.__str__
        if a1 == 'spotify':
            text1.insert('end', '[+]spotify:', 'lime')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', spotify_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="spotify acc", index=0, values=(
                'spotify', spotify_url, username, 'FOUND'))
            total_founded+=1

    def autodraw():
        global total_founded
        autodraw_url = 'https://www.autodraw.com/'
        r = requests.get(autodraw_url+username)
        soup = bc(r.content, 'html.parser')
        title35 = soup.find('title')
        a1 = title.__str__
        if a1 == 'autodraw':
            text1.insert('end', '[+]autodraw:', 'lime')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', autodraw_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="autodraw acc", index=0, values=(
                'autodraw', autodraw_url, username, 'FOUND'))
            total_founded+=1

    def figma():
        global total_founded
        figma_url = 'https://www.figma.com/'
        r = requests.get(figma_url+username)
        soup = bc(r.content, 'html.parser')
        title36 = soup.find('title')
        a1 = title.__str__
        if a1 == 'figma':
            text1.insert('end', '[+]figma:', 'pink')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', figma_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="figma acc", index=0, values=(
                'figma', figma_url, username, 'FOUND'))
            total_founded+=1

    def envision():
        global total_founded
        envision_url = 'https://www.envisionapp.com/'
        r = requests.get(envision_url+username)
        soup = bc(r.content, 'html.parser')
        title37 = soup.find('title')
        a1 = title.__str__
        if a1 == 'envision':
            text1.insert('end', '[+]envision:', 'pink')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', envision_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="envision acc", index=0, values=(
                'envision', envision_url, username, 'FOUND'))
            total_founded+=1

    def templatemonster():
        global total_founded
        monster_url = 'https://www.templatemonster.com/'
        r = requests.get(monster_url+username)
        soup = bc(r.content, 'html.parser')
        title38 = soup.find('title')
        a1 = title.__str__
        if a1 == 'monster':
            text1.insert('end', '[+]monster:', 'pink')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', monster_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="monster acc", index=0, values=(
                'monster', monster_url, username, 'FOUND'))
            total_founded +=1
    def designmodo():
        global total_founded
        mddesign_url = 'https://www.designmodo.com/'
        r = requests.get(mddesign_url+username)
        soup = bc(r.content, 'html.parser')
        title39 = soup.find('title')
        a1 = title.__str__
        if a1 == 'design modo':
            text1.insert('end', '[+]mddesign:', 'pink')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', mddesign_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="mddesign acc", index=0, values=(
                'mddesign', mddesign_url, username, 'FOUND'))
            total_founded +=1
    def houzz():
        global total_founded
        houzz_url = 'https://www.houzz.com/'
        r = requests.get(houzz_url+username)
        soup = bc(r.content, 'html.parser')
        title40 = soup.find('title')
        a1 = title.__str__
        if a1 == 'houzz':
            text1.insert('end', '[+]houzz:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', houzz_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="houzz acc", index=0, values=(
                'houzz', houzz_url, username, 'FOUND'))
            total_founded +=1

    def weebly():
        global total_founded
        weebly_url = 'https://www.weebly.com/'
        r = requests.get(weebly_url+username)
        soup = bc(r.content, 'html.parser')
        title41 = soup.find('title')
        a1 = title.__str__
        if a1 == 'weebly':
            text1.insert('end', '[+]weebly:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', weebly_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="weebly acc", index=0, values=(
                'weebly', weebly_url, username, 'FOUND'))
            total_founded +=1

    def bandcamp():
        global total_founded
        bancamp_url = 'https://www.weebly.com/'
        r = requests.get(bancamp_url+username)
        soup = bc(r.content, 'html.parser')
        title42 = soup.find('title')
        a1 = title.__str__
        if a1 == 'bancamp':
            text1.insert('end', '[+]bancamp:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', bancamp_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="bancamp acc", index=0, values=(
                'bancamp', bancamp_url, username, 'FOUND'))
            total_founded+=1

    def yandex():
        global total_founded
        yandex_url = 'https://www.yandex.com/'
        r = requests.get(yandex_url+username)
        soup = bc(r.content, 'html.parser')
        title43 = soup.find('title')
        a1 = title.__str__
        if a1 == 'yandex':
            text1.insert('end', '[+]yandex:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', yandex_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="yandex acc", index=0, values=(
                'yandex', yandex_url, username, 'FOUND'))
            total_founded+=1

    def g2g():
        global total_founded
        g2g_url = 'https://www.g2g.com/'
        r = requests.get(g2g_url+username)
        soup = bc(r.content, 'html.parser')
        title43 = soup.find('title')
        a1 = title.__str__
        if a1 == 'g2g':
            text1.insert('end', '[+]g2g:', 'yellow')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', g2g_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="g2g acc", index=0, values=(
                'g2g', g2g_url, username, 'FOUND'))
            total_founded+=1

    def udemu():
        global total_founded
        udemu_url = 'https://www.udemu.com/'
        r = requests.get(udemu_url+username)
        soup = bc(r.content, 'html.parser')
        title44 = soup.find('title')
        a1 = title.__str__
        if a1 == 'g2g':
            text1.insert('end', '[+]udemu:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', udemu_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="udemu acc", index=0, values=(
                'udemu', udemu_url, username, 'FOUND'))
            total_founded+=1

    def overflowstack():
        global total_founded
        stack_url = 'https://www.stackoverflow.com/'
        r = requests.get(stack_url+username)
        soup = bc(r.content, 'html.parser')
        title45 = soup.find('title')
        a1 = title.__str__
        if a1 == 'stackoverflow':
            text1.insert('end', '[+]stackoverflow:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', stack_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="stack acc", index=0, values=(
                'stack', stack_url, username, 'FOUND'))
            total_founded+=1

    def soundcloud():
        global total_founded
        sound_url = 'https://www.soundcloud.com/'
        r = requests.get(sound_url+username)
        soup = bc(r.content, 'html.parser')
        title46 = soup.find('title')
        a1 = title.__str__
        if a1 == 'soundcloud':
            text1.insert('end', '[+]soundcloud:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', sound_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="sound acc", index=0, values=(
                'sound', sound_url, username, 'FOUND'))
            total_founded+=1

    def skype():
        global total_founded
        skype_url = 'https://www.skype.com/'
        r = requests.get(skype_url+username)
        soup = bc(r.content, 'html.parser')
        title47 = soup.find('title')
        a1 = title.__str__
        if a1 == 'skype':
            text1.insert('end', '[+]skype:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', skype_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="skype acc", index=0, values=(
                'skype', skype_url, username, 'FOUND'))
            total_founded+=1

    def wechat():
        global total_founded
        wechat_url = 'https://www.wechat.com/'
        r = requests.get(wechat_url+username)
        soup = bc(r.content, 'html.parser')
        title48 = soup.find('title')
        a1 = title.__str__
        if a1 == 'telegram':
            text1.insert('end', '[+]wechat:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', wechat_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="wechat acc", index=0, values=(
                'wechat', wechat_url, username, 'FOUND'))
            total_founded+=1

    def telegram():
        global total_founded
        telegram_url = 'https://www.telegram.org/'
        r = requests.get(telegram_url+username)
        soup = bc(r.content, 'html.parser')
        title49 = soup.find('title')
        a1 = title.__str__
        if a1 == 'telegram':
            text1.insert('end', '[+]telegram:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', telegram_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="telegram acc", index=0, values=(
                'telegram', telegram_url, username, 'FOUND'))
            total_founded+=1

    def whatsapp():
        global total_founded
        whatsapp_url = 'https://www.whatsapp.com/'
        r = requests.get(whatsapp_url+username)
        soup = bc(r.content, 'html.parser')
        title50 = soup.find('title')
        a1 = title.__str__
        if a1 == 'whatsapp':
            text1.insert('end', '[+]whatsapp:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', whatsapp_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="whatsapp acc", index=0, values=(
                'whatsapp', whatsapp_url, username, 'FOUND'))
            total_founded+=1

    def airnb():
        global total_founded
        airnb_url = 'https://www.airbnb.com/'
        r = requests.get(airnb_url+username)
        soup = bc(r.content, 'html.parser')
        title51 = soup.find('title')
        a1 = title.__str__
        if a1 == 'airnb':
            text1.insert('end', '[+]airnb:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', airnb_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="airnb acc", index=0, values=(
                'airnb', airnb_url, username, 'FOUND'))
            total_founded+=1

    def microsoft():
        global total_founded 
        microsoft_url = 'https://www.microsoft.com/'
        r = requests.get(microsoft_url+username)
        soup = bc(r.content, 'html.parser')
        title52 = soup.find('title')
        a1 = title.__str__
        if a1 == 'airnb':
            text1.insert('end', '[+]microsoft:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', microsoft_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="microsoft acc", index=0, values=(
                'microsoft', microsoft_url, username, 'FOUND'))
            total_founded+=1

    def tumblr():
        global total_founded
        tumblr_url = 'https://www.tumblr.com/'
        r = requests.get(tumblr_url+username)
        soup = bc(r.content, 'html.parser')
        title53 = soup.find('title')
        a1 = title.__str__
        if a1 == 'tumblr':
            text1.insert('end', '[+]tumblr:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', tumblr_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="tumblr acc", index=0, values=(
                'tumblr', tumblr_url, username, 'FOUND'))
            total_founded+=1

    def vimeo():
        global total_founded
        vimeo_url = 'https://www.vimeo.com/'
        r = requests.get(vimeo_url+username)
        soup = bc(r.content, 'html.parser')
        title54 = soup.find('title')
        a1 = title.__str__
        if a1 == 'vimeo':
            text1.insert('end', '[+]vimeo:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', vimeo_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="vimeo acc", index=0, values=(
                'vimeo', vimeo_url, username, 'FOUND'))
            total_founded+=1

    def zara():
        global total_founded
        zara_url = 'https://www.zara.com/'
        r = requests.get(zara_url+username)
        soup = bc(r.content, 'html.parser')
        title55 = soup.find('title')
        a1 = title.__str__
        if a1 == 'zara':
            text1.insert('end', '[+]zara:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', zara_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="zara acc", index=0, values=(
                'zara', zara_url, username, 'FOUND'))
            total_founded+=1

    def nike():
        global total_founded
        nike_url = 'https://www.nike.com/'
        r = requests.get(nike_url+username)
        soup = bc(r.content, 'html.parser')
        title56 = soup.find('title')
        a1 = title.__str__
        if a1 == 'zara':
            text1.insert('end', '[+]nike:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', nike_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="nike acc", index=0, values=(
                'nike ', nike_url, username, 'FOUND'))
            total_founded+=1

    def asos():
        global total_founded
        asos_url = 'https://www.asos.com/'
        r = requests.get(asos_url+username)
        soup = bc(r.content, 'html.parser')
        title56 = soup.find('title')
        a1 = title.__str__
        if a1 == 'asos':
            text1.insert('end', '[+]asos:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', asos_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="asos acc", index=0, values=(
                'asos', asos_url, username, 'FOUND'))
            total_founded+=1

    def zomeus():
        global total_founded
        zome_url = 'https://www.zome.us/'
        r = requests.get(zome_url+username)
        soup = bc(r.content, 'html.parser')
        title57 = soup.find('title')
        a1 = title.__str__
        if a1 == 'zome':
            text1.insert('end', '[+]zome:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', zome_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="zome acc", index=0, values=(
                'zome', zome_url, username, 'FOUND'))
            total_founded+=1

    def icloud():
        global total_founded
        icloud_url = 'https://www.icloud.com/'
        r = requests.get(icloud_url+username)
        soup = bc(r.content, 'html.parser')
        title58 = soup.find('title')
        a1 = title.__str__
        if a1 == 'icloud':
            text1.insert('end', '[+]icloud:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', icloud_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="icloud acc", index=0, values=(
                'icloud', icloud_url, username, 'FOUND'))
            total_founded+=1

    def trello():
        global total_founded
        trello_url = 'https://www.trello.com/'
        r = requests.get(trello_url+username)
        soup = bc(r.content, 'html.parser')
        title59 = soup.find('title')
        a1 = title.__str__
        if a1 == 'trello':
            text1.insert('end', '[+]trello:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', trello_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="trello acc", index=0, values=(
                'trello', trello_url, username, 'FOUND'))
            total_founded+=1

    def asana():
        global total_founded 
        asana_url = 'https://www.asana.com/'
        r = requests.get(asana_url+username)
        soup = bc(r.content, 'html.parser')
        title60 = soup.find('title')
        a1 = title.__str__
        if a1 == 'asana':
            text1.insert('end', '[+]asana:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', asana_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="asana acc", index=0, values=(
                'asana', asana_url, username, 'FOUND'))
            total_founded+=1


    def blogger():
        global total_founded
        blogger_url = 'https://www.blogger.com'
        r = requests.get(blogger_url+username)
        soup = bc(r.content, 'html.parser')
        title62 = soup.find('title')
        a1 = title.__str__
        if a1 == 'blogger':
            text1.insert('end', '[+]blogger:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', blogger_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="blogger acc", index=0, values=(
                'blogger', blogger_url, username, 'FOUND'))
            total_founded+=1


    def pepsi():
        global total_founded
        pepsi_url = 'https://www.pepsi.com/'
        r = requests.get(pepsi_url+username)
        soup = bc(r.content, 'html.parser')
        title63 = soup.find('title')
        a1 = title.__str__
        if a1 == 'pepsi':
            text1.insert('end', '[+]pepsi:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', pepsi_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="pepsi acc", index=0, values=(
                'pepsi', pepsi_url, username, 'FOUND'))
            total_founded+=1


    def prada():
        global total_founded
        prada_url = 'https://www.prada.com/'
        r = requests.get(prada_url+username)
        soup = bc(r.content, 'html.parser')
        title63 = soup.find('title')
        a1 = title.__str__
        if a1 == 'prada':
            text1.insert('end', '[+]prada:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', prada_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="prada acc", index=0, values=(
                'prada', prada_url, username, 'FOUND'))
            total_founded+=1

    def gucci():
        global total_founded
        gucci_url = 'https://www.gucci.com/'
        r = requests.get(gucci_url+username)
        soup = bc(r.content, 'html.parser')
        title64 = soup.find('title')
        a1 = title.__str__
        if a1 == 'gucci':
            text1.insert('end', '[+]gucci:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', gucci_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="gucci acc", index=0, values=(
                'gucci', gucci_url, username, 'FOUND'))
            total_founded+=1


    def chanel():
        global total_founded
        channel_url = 'https://www.chanel.com/'
        r = requests.get(channel_url+username)
        soup = bc(r.content, 'html.parser')
        title65 = soup.find('title')
        a1 = title.__str__
        if a1 == 'channel':
            text1.insert('end', '[+]channel:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', channel_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="channel acc", index=0, values=(
                'channel', channel_url, username, 'FOUND'))
            total_founded+=1


    def samsung():
        global total_founded
        samsung_url = 'https://www.samsung.com/'
        r = requests.get(samsung_url+username)
        soup = bc(r.content, 'html.parser')
        title66 = soup.find('title')
        a1 = title.__str__
        if a1 == 'samsung':
            text1.insert('end', '[+]samsung:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', samsung_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="samsung acc", index=0, values=(
                'samsung', samsung_url, username, 'FOUND'))
            total_founded+=1


    def techno():
        global total_founded
        techno_url = 'https://www.techno-mobile.com/'
        r = requests.get(techno_url+username)
        soup = bc(r.content, 'html.parser')
        title67 = soup.find('title')
        a1 = title.__str__
        if a1 == 'samsung':
            text1.insert('end', '[+]techno:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', techno_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="techno acc", index=0, values=(
                'techno', techno_url, username, 'FOUND'))
            total_founded+=1


    def school():
        global total_founded
        school_url = 'https://www.w3schools.com/'
        r = requests.get(school_url+username)
        soup = bc(r.content, 'html.parser')
        title68 = soup.find('title')
        a1 = title.__str__
        if a1 == 'w3schools':
            text1.insert('end', '[+]w3schools:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', school_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="w3schools acc", index=0, values=(
                'w3schools', school_url, username, 'FOUND'))
            total_founded+=1


    def code():
        global total_founded
        code_url = 'https://www.code.org/'
        r = requests.get(code_url+username)
        soup = bc(r.content, 'html.parser')
        title69 = soup.find('title')
        a1 = title.__str__
        if a1 == 'code':
            text1.insert('end', '[+]code:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', code_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="code acc", index=0, values=(
                'code', code_url, username, 'FOUND'))
            total_founded+=1


    def codecademy():
        global total_founded
        codecademy_url = 'https://www.codecademy.com/'
        r = requests.get(codecademy_url+username)
        soup = bc(r.content, 'html.parser')
        title70 = soup.find('title')
        a1 = title.__str__
        if a1 == 'codecademy':
            text1.insert('end', '[+]codecademy:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', codecademy_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="codecademy acc", index=0, values=(
                'codec', codecademy_url, username, 'FOUND'))
            total_founded+=1
            threading.Thread(target=calctotalwebsitefounded).start()

   
    
    threading.Thread(target=chanel).start()
    threading.Thread(target=codecademy).start()
    threading.Thread(target=school).start()
    threading.Thread(target=code).start()
    threading.Thread(target=samsung).start()
    threading.Thread(target=gucci).start()
    threading.Thread(target=aub).start()
    threading.Thread(target=pepsi).start()
    threading.Thread(target=techno).start()
    threading.Thread(target=icloud).start()
    threading.Thread(target=prada).start()
#    ===================
    threading.Thread(target=asana).start()
    threading.Thread(target=blogger).start()
    threading.Thread(target=nike).start()
    threading.Thread(target=trello).start()
    threading.Thread(target=asos).start()
    threading.Thread(target=zomeus).start()
    threading.Thread(target=tumblr).start()
    threading.Thread(target=vimeo).start()
    threading.Thread(target=microsoft).start()
    threading.Thread(target=skype).start()
    # ==========================================
    threading.Thread(target=airnb).start()
    threading.Thread(target=zara).start()
    threading.Thread(target=telegram).start()
    threading.Thread(target=whatsapp).start()
    threading.Thread(target=wechat).start()
    threading.Thread(target=bandcamp).start()
    threading.Thread(target=udemu).start()
    threading.Thread(target=yandex).start()
    threading.Thread(target=overflowstack).start()
    threading.Thread(target=weebly).start()
    # ======================new data======================
    threading.Thread(target=g2g).start()
    threading.Thread(target=designmodo).start()
    threading.Thread(target=envision).start()
    threading.Thread(target=houzz).start()
    threading.Thread(target=autodraw).start()
    threading.Thread(target=ebay).start()
    threading.Thread(target=twicth).start()
    threading.Thread(target=templatemonster).start()
    threading.Thread(target=tiktok).start()
    threading.Thread(target=spotify).start()
    threading.Thread(target=figma).start()
    threading.Thread(target=amut).start()
    threading.Thread(target=mubs).start()
    threading.Thread(target=ndu).start()
    threading.Thread(target=usj).start()
    threading.Thread(target=balamand).start()
    threading.Thread(target=ua).start()
    threading.Thread(target=mtv).start()
    threading.Thread(target=aljadeed).start()
    threading.Thread(target=liu).start()
    threading.Thread(target=ul).start()
    threading.Thread(target=bau).start()
    threading.Thread(target=spacex).start()
    threading.Thread(target=soundcloud).start()
    threading.Thread(target= dropbox).start()
    threading.Thread(target= jinan).start()
    threading.Thread(target= aut).start()
    threading.Thread(target= face).start()
    threading.Thread(target= tinkercad).start()
    threading.Thread(target= freelancer).start()
    threading.Thread(target=github).start()
    threading.Thread(target=chatgpt).start()
    threading.Thread(target=tesla).start()
    threading.Thread(target=chatgpt).start()
    threading.Thread(target=google).start()
    threading.Thread(target=snapchat).start()
    threading.Thread(target=youtube).start()
    threading.Thread(target=amazon).start()
    threading.Thread(target=instagram).start()
    threading.Thread(target=linkedin).start()
    threading.Thread(target=netflix).start()
    threading.Thread(target=discord).start()
    threading.Thread(target=twitter).start()
    threading.Thread(target=fiverr).start()
    threading.Thread(target=reddit).start()
    threading.Thread(target=pinterest).start()
    threading.Thread(target=canva).start()
    threading.Thread(target=designevo).start()
    threading.Thread(target=canva).start()
    threading.Thread(target=logojoy).start()
def calctotalwebsitefounded():
    from tkinter import messagebox
    messagebox.showinfo("Variable Value",total_founded)
# =============button====================
imagelabs=PhotoImage(file="images1.png",width=190,height=50)

button1 = Button(root, text='start testing', 
                 height=2, cursor='hand2', bg='royalblue', fg='white', command=data,font=("Verdana",9))
button1.place(x=0, y=513,width=190,height=40)


def exit():
    from tkinter import messagebox
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()
    else:
        root.mainloop()
   


def startsearching():
    exit()
    import tkinter
    import re
    from tkinter import messagebox
    window = Tk()
    window.geometry("900x500+200+100")
    window.iconbitmap("download.ico")
    window.title("searching by her phone nb")
    window.resizable(False, False)
    frame = Frame(window)
    frame.place(x=0, y=0, width=230, height=500)
    addimage = PhotoImage(file="images1.png")
    labelimage = Label(frame, image=addimage)
    labelimage.place(x=0, y=0, width=230, height=350)

    # ====================buttons frame===========================
    buttonsframe = Frame(window)
    buttonsframe.place(x=0, y=350, width=230, height=250)
    labetitle = Label(buttonsframe, text="phnb:",
                      fg="#222", font=("Courier", 13))
    labetitle.place(x=3, y=23)
    labelsph = Entry(buttonsframe)
    labelsph.place(x=60, y=20, width=200, height=30)

    

def opentesting():
    from tkinter import messagebox
    def destroymain():
        root.destroy()
    
    import subprocess
    if messagebox.askokcancel("", "Are you sure you want to search by nb?"):
        subprocess.Popen(["python","testting.py"])
        destroymain()
    else:
        root.mainloop()

button2 = Button(root,  text=" Exit",cursor="hand2",
                 bg="red", fg="white", command=exit,font=("Verdana",9))
button2.place(x=0, y=460, width=190, height=40)
# button3
button3 = Button(root, text="search by phnb", fg="white",
                 bg="#222",command=opentesting,font=("Verdana",9))
button3.place(x=0, y=410, width=190, height=40)
# ============treview==============
tv = ttk.Treeview(root)
style = ttk.Style(root)
style.theme_use('clam')
style.configure('Treeview', rowheight=35, background='#d8d8d8',
                fieldbackground='#d8d8d8', foreground='black')
tv['columns'] = ('namesocial', 'urlname', 'username', 'status')
tv.column('#0', anchor=CENTER, width=50)
tv.column('namesocial', anchor=CENTER, width=40)
tv.column('urlname', anchor=CENTER, width=130)
tv.column('username', anchor=CENTER, width=120)
tv.column('status', anchor=CENTER, width=30)
tv.heading('#0', text='website acc', anchor=CENTER)
tv.heading('namesocial', text='website name', anchor=CENTER)
tv.heading('urlname', text='wbesite', anchor=CENTER)
tv.heading('username', text='user name', anchor=CENTER)
tv.heading('status', text='status', anchor=CENTER)
tv.place(x=200, y=35, width=765, height=550)
taha = sc.ScrolledText(tv)
text1 = sc.ScrolledText(root)
text1['font'] = ('Courier', '10', 'bold')
text1.place(x=205, y=440, width=760, height=0)
# function


root.mainloop()
