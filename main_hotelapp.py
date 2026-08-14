from tkinter import *
from PIL import Image, ImageTk
from about_us import about_page
from gallery import gallery_page
from bookingapp import booking_page
from signup import signup_page
from signin import login_page
from admin import admin_page
import session
from tkinter import messagebox as msg
from services.monitor_service import monitor_application


# WINDOW 
top = Tk()
top.title("Luxury Hotel")
top.geometry("1200x650+100+0")
top.resizable(False, False)

# TO AUTOMATICALLY FIT THE SCREEN
# screen_width = top.winfo_screenwidth()
# screen_height = top.winfo_screenheight()

# top.geometry(f"{screen_width}x{screen_height}")

# NAVBAR 
navbar = Frame(top, bg="#0b132b", height=80, width=1000)
navbar.pack(side=TOP, fill=X)

# TITLE
title = Label(navbar, text="LUXURY HOTEL", font=("Verdana", 20, "bold"),
              fg="gold", bg="#0b132b")
title.place(x=20, y=20)

# NAV BUTTONS
def nav_style(btn):
    btn.config(font=("Verdana", 10, "bold"),
               bg="#0b132b",
               fg="white",
               bd=0,
               activebackground="#1c2541",
               activeforeground="gold",
               cursor="hand2")

btn_about = Button(navbar, text="About Us", command= lambda: show_page(about_frame))
btn_gallery = Button(navbar, text="Gallery", command= lambda: show_page(gallery_frame))

# SECURE BOOKING WITHOUT SIGNUP/LOGIN
def booking():

    if session.current_user is None:

        msg.showwarning(
            "Unauthorized",
            "Please login first before booking a room."
        )

        show_page(login_frame)

    else:

        clear_bookings()
        show_page(booking_frame)

btn_booking = Button(
    navbar,
    text="Booking",
    command=booking
)
btn_signup = Button(navbar, text="Sign Up", command= lambda: show_page(signup_frame))
btn_login = Button(navbar, text="Login", command= lambda: show_page(login_frame))

buttons = [btn_about, btn_gallery, btn_booking, btn_signup, btn_login]

x_pos = 400
for btn in buttons:
    nav_style(btn)
    btn.place(x=x_pos, y=30)
    x_pos += 90





# MAIN CONTAINER
main_frame = Frame(top)
main_frame.pack(fill=BOTH, expand=True)


# USERNAME UPDATE FUNCTION
def update_user_label():

    if session.current_user is None:
        user_label.config(text="")
    else:
        user_label.config(
            text=f"Welcome, {session.current_user}"
        )


# FUNCTION TO SWITCH PAGES
def show_page(page):

    # Hide all pages
    home_page.pack_forget()
    about_frame.pack_forget()
    gallery_frame.pack_forget()
    booking_frame.pack_forget()
    signup_frame.pack_forget()
    login_frame.pack_forget()
    admin_frame.pack_forget()

    # Show selected page
    page.pack(fill=BOTH, expand=True)


# PAGES
home_page = Frame(main_frame)

about_frame = about_page(
    main_frame,
    lambda: show_page(home_page)
)

gallery_frame = gallery_page(main_frame)

booking_frame, clear_bookings = booking_page(main_frame)

signup_frame = signup_page(
    main_frame,
    lambda: show_page(login_frame)
)

login_frame = login_page(
    main_frame,
    lambda: show_page(signup_frame),
    lambda: [
        update_user_label(),
        clear_bookings(),
        show_page(home_page)
    ]
)

admin_frame = admin_page(main_frame)


# NAVIGATION FUNCTIONS

def home():
    show_page(home_page)


def aboutUs():
    show_page(about_frame)


def gallery():
    show_page(gallery_frame)


# ADMIN DASHBOARD FUNCTION/PROTECTION
def adminDashboard():

    if session.current_user is None:

        msg.showwarning(
            "Unauthorized",
            "Please login first."
        )

        show_page(login_frame)

    elif session.current_role != "admin":

        msg.showerror(
            "Access Denied",
            "Only admin can access dashboard."
        )

    else:

        show_page(admin_frame)

# BACK TO HOME PAGE
def back_page():
    show_page(home_page)


# LOGOUT FUNCTION

def logout():

    clear_bookings()

    session.current_user = None
    session.current_role = None

    update_user_label()

    msg.showinfo(
        "Logout",
        "Logged out successfully"
    )

    show_page(home_page)

# BACK BUTTON
btn_back = Button(
    navbar,
    text="← Back",
    font=("Verdana", 10, "bold"),
    bg="gold",
    fg="black",
    bd=0,
    cursor="hand2",
    command=back_page
)

btn_back.place(x=1120, y=28)


# LOGOUT BUTTON

btn_logout = Button(
    navbar,
    text="Logout",
    command=logout
)
btn_logout.place(x=1040, y=30)


# DISPLAY LOGGED IN USERNAME ON NAVBAR

user_label = Label(
    navbar,
    text="",
    fg="#17f722",
    bg="#0b132b",
    font=("Verdana", 10, "bold")
)
user_label.place(x=850, y=30)

# IMAGE 
# Load image (must be 1000x520 approx to fit remaining space)

img = Image.open("luxuryhotelBgimg.png")   # your generated image
img = img.resize((1200, 570), Image.Resampling.LANCZOS)

photo = ImageTk.PhotoImage(img)

img_label = Label(home_page, image=photo)
img_label.place(x=0, y=0)

img_label.image = photo #prevents image from disappearing

# ADMIN BUTTON 
admin_btn = Button(home_page,
                   text="Admin Dashbooard",
                   font=("Verdana", 10, "bold"),
                   bg="gold",
                   fg="black",
                   cursor="hand2", command= adminDashboard)

admin_btn.place(x=20, y=520)

# START WITH HOME PAGE

show_page(home_page)

monitor_application()

top.mainloop()