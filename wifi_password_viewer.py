import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
def link_place():
 try:
   username = 'newstyle'
   password = '1q2w3e4r5t'
   url = "http://192.168.1.2/WL_WPATable.asp"
   make_connection = requests.get(url, auth=(username, password))
   soup = BeautifulSoup(make_connection.content, 'html.parser')
   soup_finder = soup.find('input', {'name': 'wl_wpa_psk'})
   password_value = soup_finder.get('value')
   return "The wifi password is: {}" .format(password_value)      
 except:
    return "something wrong, Be sure that you are connected to the wifi and the wlan is protected by password!"

def megg():
  messagebox.showinfo("info" ,link_place() )      

guu = Tk()
guu.title("password viewer")
guu.geometry("400x400")
guu.configure(background='white')
guu.resizable(width=False, height=False)

nass1 = Label(guu, text="welcome to the wifi password viewer" , fg="black", bg="white")
nass1.pack(fill=BOTH, expand=1)
nass1.place(x=50, y=15)
nass1.config(font=('times', 15, ' bold '))

zer1 = Button(guu, text="Exit", height = 3, width = 25 ,command=guu.destroy)
zer1.pack(side=BOTTOM  ,padx = 3, pady = 25)

zer2 = Button(guu, text="Show the password"  ,height = 3, width = 25, command= megg)
zer2.pack(side=LEFT)
zer2.place(x=120, y=150)

guu.mainloop()





