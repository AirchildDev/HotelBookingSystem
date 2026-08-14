from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg
import sqlite3
import bcrypt


def signup_page(parent, show_login):

    signup_frame = Frame(parent, bg="#141414", width=1200, height=650)

    # BACKGROUND IMAGE

    img = Image.open("outsidepool_edited.png")

    img = img.resize(
        (1200, 650),
        Image.Resampling.LANCZOS
    )

    photo = ImageTk.PhotoImage(img)

    bg_label = Label(signup_frame, image=photo)

    bg_label.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

    bg_label.image = photo

    # PASSWORD HASH

    def hash_password(password):

        return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    # SIGNUP FUNCTION

    def sign():

        fullname = entry2.get()
        phonenum = entry3.get()
        username = entry4.get()

        raw_password = entry5.get()

        password = hash_password(
            raw_password
        )

        if (
            fullname == ""
            or phonenum == ""
            or username == ""
            or raw_password == ""
        ):

            msg.showinfo(
                "Alert",
                "Empty Record Not Allowed!"
            )

            return

        try:

            con = sqlite3.connect("hotel.db")
            cur = con.cursor()

            cur.execute("""
            INSERT INTO users(
                fullname,
                phonenum,
                username,
                password
            )
            VALUES(?,?,?,?)
            """, (
                fullname,
                phonenum,
                username,
                password
            ))

            con.commit()
            con.close()

            msg.showinfo(
                "Alert",
                "Successfully Registered"
            )

            # CLEAR ENTRIES

            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

            show_login()     # GOES TO LOGIN PAGE

        except sqlite3.IntegrityError:

            msg.showinfo(
                "Alert",
                "Username Already Exists"
            )

    # HOVER EFFECT

    def hover(event):

        btn.config(
            bg="#8c78f0",
            fg="#ffffff"
        )

        label6.config(
            fg="#f74242"
        )

    def no_hover(event):

        btn.config(
            bg="#C58A63",
            fg="#05374B"
        )

        label6.config(
            fg="#D9E6EB"
        )

    # TITLE

    label1 = Label(
        signup_frame,
        text="Signup Now",
        font=("verdana", 28, "bold"),
        fg="#D9E6EB",
        bg="#065270"
    )

    label1.place(x=450, y=60)

    # FULLNAME

    label2 = Label(
        signup_frame,
        text="Full Name",
        font=("verdana", 12, "bold"),
        fg="#D9E6EB",
        bg="#065270"
    )

    label2.place(x=300, y=170)

    entry2 = Entry(
        signup_frame,
        width=40
    )

    entry2.place(x=500, y=175)

    # PHONE 

    label3 = Label(
        signup_frame,
        text="Phone Number",
        font=("verdana", 12, "bold"),
        fg="#D9E6EB",
        bg="#065270"
    )

    label3.place(x=300, y=230)

    entry3 = Entry(
        signup_frame,
        width=40
    )

    entry3.place(x=500, y=235)

    # USERNAME 

    label4 = Label(
        signup_frame,
        text="Username",
        font=("verdana", 12, "bold"),
        fg="#D9E6EB",
        bg="#065270"
    )

    label4.place(x=300, y=290)

    entry4 = Entry(
        signup_frame,
        width=40
    )

    entry4.place(x=500, y=295)

    # PASSWORD 

    label5 = Label(
        signup_frame,
        text="Password",
        font=("verdana", 12, "bold"),
        fg="#D9E6EB",
        bg="#065270"
    )

    label5.place(x=300, y=350)

    entry5 = Entry(
        signup_frame,
        width=40,
        show="*"
    )

    entry5.place(x=500, y=355)

    # BUTTON 

    btn = Button(
        signup_frame,
        text="Sign Up",
        font=("verdana", 12, "bold"),
        fg="#05374B",
        bg="#C58A63",
        width=20,
        command=sign,
        cursor="hand2"
    )

    btn.place(x=500, y=430)

    btn.bind("<Enter>", hover)
    btn.bind("<Leave>", no_hover)

    # LOGIN LABEL 

    label6 = Label(
        signup_frame,
        text="Already signed-up? Login",
        font=("verdana", 9, "bold"),
        fg="#D9E6EB",
        bg="#141414",
        cursor="hand2"
    )

    label6.place(x=520, y=500)

    label6.bind("<Button-1>", lambda e: show_login())
    label6.bind("<Enter>", hover)
    label6.bind("<Leave>", no_hover)

    return signup_frame