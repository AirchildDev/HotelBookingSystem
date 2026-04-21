from tkinter import *
from tkinter import ttk
import hashlib
from tkinter import messagebox as msg
import sqlite3
import subprocess

top = Tk()
top.geometry("500x500+400+100")
top.title("Signup Page")
top.configure(background= "#141414")


def signup(event=None):
    subprocess.Popen(["python", "signin.py"])


def hover(event):
    btn.config(bg= "#8c78f0", fg= "#ffffff")
    label6.config(fg= "#f74242")

def no_hover(event):
    btn.config(bg= "#af9bf7", fg= "#141414")
    label6.config(fg= "#af9bf7")


def sign():
    fullname = entry2.get()
    phonenum = entry3.get()
    username = entry4.get()

    raw_password = entry5.get()
    password = hash_password(raw_password)
    
    
    if fullname == "" or phonenum == "" or username == "" or raw_password == "" :
        msg.showinfo("alert", "Empty Record Not Allowed! Please Fill The Form.")

    else:
        con = sqlite3.connect("hotel.db")
        cur = con.cursor()
        
    try:
        cur.execute('''insert into users(fullname, phonenum, username, password)
                    values(?,?,?,?)''',(fullname, phonenum, username, password))
        con.commit()
        msg.showinfo("Alert", "Successfully Registered")
        top.destroy()
        signup()

    except sqlite3.IntegrityError:
        msg.showinfo("Alert", "Username Already Exists")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()






label1 = Label(top, text= "Signup Now", font= ("verdana", 25, "bold"), fg= "#af9bf7", bg= "#141414")
label1.grid(row= 0, column= 1, columnspan= 2)

label2 = Label(top, text= "FullName", font= ("verdana", 10, "bold"), fg= "#af9bf7", bg= "#141414")
label2.grid(row= 1, column= 0, pady= 20)

entry2 = Entry(top, width= 50)
entry2.grid(row= 1, column= 1, pady= 20)

label3 = Label(top, text= "Phone Number", font= ("verdana", 10, "bold"), fg= "#af9bf7", bg= "#141414")
label3.grid(row= 2, column= 0, pady= 20)

entry3 = Entry(top, width= 50)
entry3.grid(row= 2, column= 1, pady= 20)

label4 = Label(top, text= "Username", font=("verdana", 10, "bold"), fg= "#af9bf7", bg= "#141414")
label4.grid(row= 3, column= 0, pady= 20)

entry4 = Entry(top, width= 50)
entry4.grid(row= 3, column= 1, pady= 20)

label5 = Label(top, text= "Password", font= ("verdana", 10, "bold"), fg= "#af9bf7", bg= "#141414")
label5.grid(row= 4, column= 0, pady= 20)

entry5 = Entry(top, width= 50, show= "*")
entry5.grid(row= 4, column= 1, pady= 20)

btn = Button(top, text= "Sign-up", font= ("verdana", 10, "bold"), fg= "#141414", bg= "#af9bf7", width= 20, command= sign, cursor= "hand2")
btn.grid(row= 5, column= 0, columnspan= 2, pady= 20)

btn.bind("<Enter>", hover)
btn.bind("<Leave>", no_hover)



label6 = Label(top, text= "Already signed-up? Login", font= ("verdana", 8, "bold"), fg= "#af9bf7", bg= "#141414", cursor= "hand2")
label6.grid(row= 6, column= 1, columnspan= 2, pady= 20)

label6.bind("<Button-1>", signup)
label6.bind("<Enter>", hover)
label6.bind("<Leave>", no_hover)




top.mainloop()

