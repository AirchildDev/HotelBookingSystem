from tkinter import *
from tkinter import ttk, messagebox

from services.room_service import (
    create_room,
    get_rooms,
    update_room_record,
    delete_room_record
)
from services.booking_service import get_bookings


def admin_page(parent):

    admin_frame = Frame(parent, bg="#220f2a")
    selected_room_id = None

    admin_frame.pack(fill="both", expand=True)

    # RESET

    def reset_all():

        nonlocal selected_room_id

        selected_room_id = None

        entry_room.delete(0, END)
        combo_type.set("")
        entry_price.delete(0, END)
        combo_status.set("")
        listbox.delete(0, END)

    # ADD ROOM

    def add_room():

        room_no = entry_room.get()
        room_type = combo_type.get()
        price = entry_price.get()
        status = combo_status.get()

        if (
            room_no == ""
            or room_type == ""
            or price == ""
            or status == ""
        ):
            messagebox.showwarning(
                "Error",
                "Fill all fields"
            )
            return

        try:
            create_room(
                room_no,
                room_type,
                price,
                status
            )

            messagebox.showinfo(
                "Success",
                "Room Added"
            )

            reset_all()
            view_rooms()

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Could not add room: {error}"
            )

    # VIEW ROOMS

    def view_rooms():

        listbox.delete(0, END)

        rows = get_rooms()

        if not rows:
            listbox.insert(END, "No rooms found")
            return

        for row in rows:
            display = f"{row[0]} | Room {row[1]} | {row[2]} | ₦{row[3]} | {row[4]}"

            listbox.insert(END, display)

    # SELECT ROOM

    def select_room(event):

        nonlocal selected_room_id

        if not listbox.curselection():
            return

        selected = listbox.get(listbox.curselection())

        if "No rooms found" in selected:
            return

        data = selected.split(" | ")

        selected_room_id = data[0]

        room_number = data[1].replace("Room ", "").strip()
        room_type = data[2].strip()
        price = data[3].replace("₦", "").strip()
        status = data[4].strip()

        entry_room.delete(0, END)
        entry_room.insert(0, room_number)

        combo_type.set(room_type)

        entry_price.delete(0, END)
        entry_price.insert(0, price)

        combo_status.set(status)

    # UPDATE ROOM

    def update_room():

        if selected_room_id is None:
            messagebox.showwarning(
                "Warning",
                "Select a room first"
            )
            return

        room_id = selected_room_id

        room_no = entry_room.get().strip()
        room_type = combo_type.get().strip()
        price = entry_price.get().strip()
        status = combo_status.get().strip()

        if (
            room_no == ""
            or room_type == ""
            or price == ""
            or status == ""
        ):
            messagebox.showwarning(
                "Warning",
                "Fill all fields"
            )
            return

        try:

            update_room_record(
                room_id,
                room_no,
                room_type,
                price,
                status
            )

            messagebox.showinfo(
                "Success",
                "Room Updated Successfully"
            )

            reset_all()
            view_rooms()

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Could not update room: {error}"
            )

    # DELETE ROOM

        # DELETE ROOM

    def delete_room():

        if selected_room_id is None:

            messagebox.showwarning(
                "Warning",
                "Select a room first"
            )

            return

        room_id = selected_room_id

        try:

            delete_room_record(room_id)

            messagebox.showinfo(
                "Deleted",
                "Room Deleted Successfully"
            )

            reset_all()
            view_rooms()

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Could not delete room: {error}"
            )

# ALLOWS THE ADMIN TO SEE USERS ACTIVITY

    def view_bookings():

        booking_tree.delete(*booking_tree.get_children())

        rows = get_bookings()

        for row in rows:

            booking_tree.insert(
                "",
                END,
                values=row
            )       

    # TITLE 

    title = Label(
        admin_frame,
        text="HOTEL ADMIN DASHBOARD",
        font=("verdana", 20, "bold"),
        fg="white",
        bg="#0f172a"
    )

    title.pack(pady=10)

    content_frame = Frame(admin_frame, bg="#220f2a")
    content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    left_frame = Frame(content_frame, bg="#220f2a")
    left_frame.pack(side=LEFT, fill="both", expand=True, padx=15, pady=10)

    right_frame = Frame(content_frame, bg="#220f2a")
    right_frame.pack(side=RIGHT, fill="both", expand=True, padx=15, pady=10)

    # FORM FRAME 

    frame = Frame(left_frame, bg="#7e0db3")
    frame.pack(pady=10, fill= "x")


    # ROOM NUMBER

    Label(
        frame,
        text="Room No",
        fg="white",
        bg="#0f172a"
    ).grid(row=0, column=0, pady=10)

    entry_room = Entry(frame)

    entry_room.grid(row=0, column=1)

    # ROOM TYPE

    Label(
        frame,
        text="Room Type",
        fg="white",
        bg="#0f172a"
    ).grid(row=1, column=0, pady=10)

    combo_type = ttk.Combobox(frame, values=["Standard", "Deluxe", "Suite"], state="readonly")
    combo_type.grid(row=1, column=1)

    # PRICE

    Label(
        frame,
        text="Price",
        fg="white",
        bg="#0f172a"
    ).grid(row=2, column=0, pady=10)

    entry_price = Entry(frame)

    entry_price.grid(row=2, column=1)

    # STATUS

    Label(
        frame,
        text="Status",
        fg="white",
        bg="#0f172a"
    ).grid(row=3, column=0, pady=10)

    combo_status = ttk.Combobox(frame, values=["Available", "Booked"], state= "readonly")
    combo_status.grid(row=3, column=1)

    # BUTTONS

    btn_frame = Frame(left_frame, bg="#0f172a")
    btn_frame.pack(pady=10, fill= "x")

    Button(
        btn_frame,
        text="Add Room",
        width=15,
        command=add_room
    ).grid(row=0, column=0, padx=5)

    Button(
        btn_frame,
        text="Update Room",
        width=15,
        command=update_room
    ).grid(row=0, column=1, padx=5)

    Button(
        btn_frame,
        text="Delete Room",
        width=15,
        command=delete_room
    ).grid(row=0, column=2, padx=5)

    Button(
        btn_frame,
        text="View Rooms",
        width=15,
        command=view_rooms
    ).grid(row=0, column=3, padx=5)

    Button(
        btn_frame,
        text="View Bookings",
        width=15,
        command=view_bookings
    ).grid(row=0, column=4, padx=5)

       # LISTBOX 

    listbox_frame = Frame(left_frame, bg="#220f2a")
    listbox_frame.pack(fill="both", expand=True)

    listbox = Listbox(listbox_frame)
    listbox.pack(pady=10, fill= "both", expand= True)

    listbox.bind(
        "<<ListboxSelect>>",
        select_room
    )
 

# BOOKING TABLE 
# TITLE

    booking_label = Label(
    right_frame,
    text="USER BOOKINGS / ACTIVITIES",
    font=("verdana", 14, "bold"),
    fg="white",
    bg="#220f2a"
    )
    booking_label.pack(pady=10)

# BOOKING TREEVIEW
    booking_tree = ttk.Treeview(
    right_frame,
    columns=("ID", "Room", "Customer", "Check In", "Check Out", "Username"),
    show="headings",
    height=18
)

    booking_tree.heading("ID", text="ID")
    booking_tree.heading("Room", text="Room")
    booking_tree.heading("Customer", text="Customer")
    booking_tree.heading("Check In", text="Check In")
    booking_tree.heading("Check Out", text="Check Out")
    booking_tree.heading("Username", text="Username")

    booking_tree.column("ID", width=50)
    booking_tree.column("Room", width=100)
    booking_tree.column("Customer", width=200)
    booking_tree.column("Check In", width=120)
    booking_tree.column("Check Out", width=120)
    booking_tree.column("Username", width=120)

    booking_tree.pack(
    pady=10,
    fill="both",
    expand=True
)

# START DASHBOARD
    reset_all()
    view_rooms()
    view_bookings()

    return admin_frame