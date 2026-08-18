from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from database.connection import get_connection
import session
import bcrypt


def login_page(parent, show_signup, show_home):

    login_frame = Frame(
        parent,
        bg="#80050b",
        width=1200,
        height=650
    )

    # BACKGROUND IMAGE

    img = Image.open("lounge_dark_blur.jpg")
    img = img.resize(
        (1200, 650),
        Image.Resampling.LANCZOS
    )

    photo = ImageTk.PhotoImage(img)

    bg_label = Label(
        login_frame,
        image=photo
    )

    bg_label.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

    bg_label.image = photo

    # LOGIN FUNCTION

    def login():

        username = entry1.get().strip()
        password = entry2.get()

        if username == "" or password == "":

            msg.showinfo(
                "Alert",
                "Enter your username and password"
            )

            return

        try:

            con = get_connection()
            cur = con.cursor()

            # GET USER BY USERNAME

            cur.execute("""
                SELECT username, role, password
                FROM users
                WHERE username = %s
            """, (username,))

            result = cur.fetchone()

            cur.close()
            con.close()

            # CHECK PASSWORD

            if result and bcrypt.checkpw(
                password.encode("utf-8"),
                result[2].encode("utf-8")
            ):

                session.current_user = result[0]
                session.current_role = result[1]

                msg.showinfo(
                    "Alert",
                    "Login Successful"
                )

                # CLEAR ENTRIES

                entry1.delete(0, END)
                entry2.delete(0, END)

                show_home()

            else:

                msg.showwarning(
                    "Warning",
                    "Unauthorized Access"
                )

        except Exception as error:

            msg.showerror(
                "Database Error",
                f"Unable to connect to database:\n{error}"
            )

    # HOVER EFFECT

    def hover(event):
        label3.config(fg="#aaa00c")

    def no_hover(event):
        label3.config(fg="#f5e173")

    # TITLE

    label = Label(
        login_frame,
        text="LOGIN",
        font=("verdana", 24, "bold"),
        fg="#ffffff",
        bg="#000000"
    )

    label.place(x=500, y=100)

    # USERNAME

    label1 = Label(
        login_frame,
        text="Username",
        font=("verdana", 12, "bold"),
        fg="#ffffff",
        bg="#000000"
    )

    label1.place(x=380, y=200)

    entry1 = Entry(
        login_frame,
        width=40
    )

    entry1.place(x=520, y=205)

    # PASSWORD

    label2 = Label(
        login_frame,
        text="Password",
        font=("verdana", 12, "bold"),
        fg="#ffffff",
        bg="#000000"
    )

    label2.place(x=380, y=260)

    entry2 = Entry(
        login_frame,
        width=40,
        show="*"
    )

    entry2.place(x=520, y=265)

    # LOGIN BUTTON

    login_btn = Button(
        login_frame,
        text="Login",
        font=("verdana", 12, "bold"),
        fg="#80050b",
        bg="#f5e173",
        width=15,
        command=login,
        cursor="hand2"
    )

    login_btn.place(x=520, y=330)

    # SIGNUP LABEL

    label3 = Label(
        login_frame,
        text="Not yet signed up? Click here",
        font=("verdana", 9, "bold"),
        fg="#f5e173",
        bg="#000000",
        cursor="hand2"
    )

    label3.place(x=520, y=390)

    label3.bind("<Enter>", hover)
    label3.bind("<Leave>", no_hover)
    label3.bind(
        "<Button-1>",
        lambda e: show_signup()
    )

    return login_frame