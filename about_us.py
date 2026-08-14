from tkinter import *

# ABOUT PAGE FUNCTION 
def about_page(main_frame, show_home):

    # PAGE FRAME
    about_frame = Frame(main_frame, bg="#0b132b")

    # MAIN CONTAINER 
    container = Frame(about_frame)
    container.pack(fill=BOTH, expand=1)

    # CANVAS 
    canvas = Canvas(container, bg="#0b132b", highlightthickness=0)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # SCROLLBAR 
    scrollbar = Scrollbar(container, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # SECOND FRAME 
    second_frame = Frame(canvas, bg="#0b132b")

    canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # HEADER 
    header = Frame(second_frame, bg="#1c2541", height=80)
    header.pack(fill=X)

    title = Label(
        header,
        text="LUXURY HOTEL",
        font=("Verdana", 24, "bold"),
        fg="gold",
        bg="#1c2541"
    )
    title.place(x=30, y=20)

    # BACK BUTTON 
    back_btn = Button(
        header,
        text="← Back",
        font=("Verdana", 10, "bold"),
        bg="gold",
        fg="black",
        cursor="hand2",
        command=show_home
    )
    back_btn.place(x=1000, y=25)

    # ABOUT TITLE
    about_title = Label(
        second_frame,
        text="ABOUT US",
        font=("Verdana", 30, "bold"),
        fg="gold",
        bg="#0b132b"
    )
    about_title.pack(pady=20)

    # ABOUT TEXT 
    about_text = """
Welcome to Luxury Hotel — where elegance meets comfort.

Luxury Hotel is designed to provide a world-class experience
for guests seeking relaxation, comfort, and unforgettable moments.

Our hotel features:
• Luxury suites and executive rooms
• Rooftop swimming pool
• Premium restaurant and bar
• Spa and wellness center
• Conference and event halls
• 24/7 room service
• Airport pickup services
• High-speed Wi-Fi connectivity

At Luxury Hotel, we combine modern architecture,
premium hospitality, and exceptional customer care
to create a perfect destination for business travelers,
tourists, couples, and families.
"""

    description = Label(
        second_frame,
        text=about_text,
        font=("Verdana", 13),
        fg="white",
        bg="#0b132b",
        justify=LEFT,
        wraplength=850
    )

    description.pack(padx=40, pady=10)

    # FEATURES 
    features_frame = Frame(second_frame, bg="#1c2541")
    features_frame.pack(pady=30, padx=40, fill=X)

    features_title = Label(
        features_frame,
        text="WHY CHOOSE US",
        font=("Verdana", 20, "bold"),
        fg="gold",
        bg="#1c2541"
    )

    features_title.pack(pady=15)

    features = [
        "✔ Elegant Luxury Rooms",
        "✔ Rooftop Swimming Pool",
        "✔ Fine Dining Restaurant",
        "✔ 24/7 Room Service",
        "✔ Airport Pickup",
        "✔ Maximum Security",
        "✔ Spa & Wellness Center"
    ]

    for feature in features:
        Label(
            features_frame,
            text=feature,
            font=("Verdana", 12),
            fg="white",
            bg="#1c2541"
        ).pack(anchor="w", padx=30, pady=5)

    # FOOTER 
    footer = Label(
        second_frame,
        text="© 2026 Luxury Hotel. All Rights Reserved.",
        font=("Verdana", 10),
        fg="white",
        bg="#0b132b"
    )

    footer.pack(pady=30)

    # MOUSE SCROLL 
    def mouse_scroll(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", mouse_scroll)

    return about_frame