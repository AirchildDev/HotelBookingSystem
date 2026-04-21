from tkinter import *
import subprocess
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3 
import hashlib       

top = Tk()
top.geometry("400x300+200+100")
top.title("Login Page")
top.configure(background= "#80050b")

def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" or password == "":
        msg.showinfo("Alert", "Enter your username and password")
        return
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    result = cur.fetchone()
    con.close()

    if result:
        msg.showinfo("Alert", "Login Successful")
        top.destroy()
        subprocess.Popen(["python", "bookingapp.py"])
    else:
        msg.showwarning("Warning", "Unauthorized Access")


def signup(event=None):
    subprocess.Popen(["python", "signup.py"])



def hover(event):
    label3.config(fg= "#aaa00c")

def no_hover(event):
    label3.config(fg= "#f5e173")



label = Label(top, text= "LOGIN", font= ("verdana", 20, "bold"), fg= "#f5e173", bg= "#80050b")
label.place(x= 130, y= 0)

label1 = Label(top, text= "Username", font= ("verdana", 12, "bold"), fg= "#f5e173", bg= "#80050b")
label1.place(x= 10, y= 50)

entry1 = Entry(top, width= 40)
entry1.place(x= 120, y= 50)

label2 = Label(top, text= "Password", font= ("verdana", 12, "bold"), fg= "#f5e173", bg= "#80050b")
label2.place(x= 10, y= 100)

entry2 = Entry(top, width= 40, show= "*")
entry2.place(x= 120, y= 100)

login_btn = Button(top, text= "Login", font= ("verdana", 12, "bold"), fg= "#80050b", bg= "#f5e173", width= 10, command= login)
login_btn.place(x= 120, y= 150)


label3 = Label(top, text= "Not yet signed up? Click here", font= ("verdana", 8, "bold"), fg= "#ffffff", bg= "#80050b", cursor= "hand2")
label3.place(x= 120, y= 200)

label3.bind("<Button-1>", signup)
label3.bind("<Enter>", hover)
label3.bind("<Leave>", no_hover)



top.mainloop()
