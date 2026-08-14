from tkinter import *
from PIL import Image, ImageTk

def gallery_page(parent):

    gallery_frame = Frame(parent, bg="#0b132b")

    # ================= HEADER =================
    header = Frame(gallery_frame, bg="#1c2541", height=80)
    header.pack(fill=X)

    title = Label(
        header,
        text="LUXURY HOTEL GALLERY",
        font=("Verdana", 24, "bold"),
        fg="gold",
        bg="#1c2541"
    )
    title.place(x=20, y=20)

    # ================= GALLERY CONTAINER =================
    images_frame = Frame(gallery_frame, bg="#0b132b")
    images_frame.pack(pady=20)

    # ================= LOAD IMAGES =================

    img1 = Image.open("lounge1.jpg")
    img1 = img1.resize((280, 180))
    photo1 = ImageTk.PhotoImage(img1)

    img2 = Image.open("outsidepool.jpg")
    img2 = img2.resize((280, 180))
    photo2 = ImageTk.PhotoImage(img2)

    img3 = Image.open("lounge.jpg")
    img3 = img3.resize((280, 180))
    photo3 = ImageTk.PhotoImage(img3)

    img4 = Image.open("yacht.jpg")
    img4 = img4.resize((280, 180))
    photo4 = ImageTk.PhotoImage(img4)

    img5 = Image.open("lounge_area.jpg")
    img5 = img5.resize((280, 180))
    photo5 = ImageTk.PhotoImage(img5)

    img6 = Image.open("poolside2.jpg")
    img6 = img6.resize((280, 180))
    photo6 = ImageTk.PhotoImage(img6)

    # ================= IMAGE LABELS =================

    label1 = Label(images_frame, image=photo1, bd=3, relief=RIDGE)
    label1.grid(row=0, column=0, padx=15, pady=15)

    label2 = Label(images_frame, image=photo2, bd=3, relief=RIDGE)
    label2.grid(row=0, column=1, padx=15, pady=15)

    label3 = Label(images_frame, image=photo3, bd=3, relief=RIDGE)
    label3.grid(row=0, column=2, padx=15, pady=15)

    label4 = Label(images_frame, image=photo4, bd=3, relief=RIDGE)
    label4.grid(row=1, column=0, padx=15, pady=15)

    label5 = Label(images_frame, image=photo5, bd=3, relief=RIDGE)
    label5.grid(row=1, column=1, padx=15, pady=15)

    label6 = Label(images_frame, image=photo6, bd=3, relief=RIDGE)
    label6.grid(row=1, column=2, padx=15, pady=15)

    # Prevent images from disappearing
    label1.image = photo1
    label2.image = photo2
    label3.image = photo3
    label4.image = photo4
    label5.image = photo5
    label6.image = photo6

    # ================= FOOTER =================

    footer = Label(
        gallery_frame,
        text="© 2026 Luxury Hotel Gallery",
        font=("Verdana", 10),
        fg="white",
        bg="#0b132b"
    )
    footer.pack(side=BOTTOM, pady=10)

    return gallery_frame