from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import sqlite3

top = Tk()
top.title("Hotel Booking Page")
top.geometry("900x600")
top.configure(bg="#0b132b")


# LOAD AVAILABLE ROOMS 
def load_rooms():
    combo_room['values'] = []

    check_in = cal_in.get_date()
    check_out = cal_out.get_date()

    con = sqlite3.connect("hotel.db")
    cur = con.cursor()

    cur.execute("SELECT room_number FROM rooms")
    rooms = cur.fetchall()

    available_rooms = []

    for r in rooms:
        if is_room_available(r[0], str(check_in), str(check_out)):
            available_rooms.append(r[0])

    combo_room['values'] = available_rooms

    con.close()


#  CHECK DOUBLE BOOKING 

def is_room_available(room, check_in, check_out):
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()

    cur.execute("""
    SELECT * FROM bookings
    WHERE room_number = ?
    AND NOT (
        check_out <= ?
        OR check_in >= ?
    )
    """, (room, check_in, check_out))

    result = cur.fetchone()
    con.close()

    return result is None


#  BOOK ROOM 
def book_room():
    name = entry_name.get()
    room = combo_room.get()
    check_in = cal_in.get_date()
    check_out = cal_out.get_date()

    if name == "" or room == "":
        messagebox.showwarning("Error", "Fill all fields")
        return

    if check_in >= check_out:
        messagebox.showwarning("Error", "Check-out must be after check-in")
        return

    if not is_room_available(room, str(check_in), str(check_out)):
        messagebox.showerror("Error", "Room already booked for selected dates")
        return

    con = sqlite3.connect("hotel.db")
    cur = con.cursor()

    cur.execute("""
    INSERT INTO bookings(room_number, customer_name, check_in, check_out)
    VALUES(?,?,?,?)
    """, (room, name, check_in, check_out))

    con.commit()
    con.close()

    messagebox.showinfo("Success", "Room booked successfully")

    view_bookings()
    load_rooms()

    entry_name.delete(0, END)
    combo_room.set("")

#  VIEW BOOKINGS
def view_bookings():
    listbox.delete(0, END)

    con = sqlite3.connect("hotel.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM bookings")
    rows = cur.fetchall()

    for row in rows:
        display = f"{row[0]} | Room {row[1]} | {row[2]} | {row[3]} to {row[4]}"
        listbox.insert(END, display)

    con.close()

#  UI 

title = Label(top, text="HOTEL RESERVATION SYSTEM", font=("verdana", 20, "bold"),
              fg="white", bg="#0b132b")
title.pack(pady=10)

frame = Frame(top, bg="#0b132b")
frame.pack(pady=10)

# NAME
Label(frame, text="Customer Name", fg="white", bg="#0b132b").grid(row=0, column=0)
entry_name = Entry(frame)
entry_name.grid(row=0, column=1)

# ROOM
Label(frame, text="Select Room", fg="white", bg="#0b132b").grid(row=1, column=0)
combo_room = ttk.Combobox(frame)
combo_room.grid(row=1, column=1)

# CHECK-IN
Label(frame, text="Check-In Date", fg="white", bg="#0b132b").grid(row=2, column=0)
cal_in = DateEntry(frame, width=12, background='darkblue', foreground='white')
cal_in.grid(row=2, column=1)

# CHECK-OUT
Label(frame, text="Check-Out Date", fg="white", bg="#0b132b").grid(row=3, column=0)
cal_out = DateEntry(frame, width=12, background='darkblue', foreground='white')
cal_out.grid(row=3, column=1)

# BIND AFTER CREATION
cal_in.bind("<<DateEntrySelected>>", lambda e: load_rooms())
cal_out.bind("<<DateEntrySelected>>", lambda e: load_rooms())

# BUTTONS
btn_frame = Frame(top, bg="#0b132b")
btn_frame.pack(pady=10)

Button(btn_frame, text="Book Room", width=15, command=book_room).grid(row=0, column=0, padx=5)
Button(btn_frame, text="View Bookings", width=15, command=view_bookings).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Refresh Rooms", width=15, command=load_rooms).grid(row=0, column=2, padx=5)

# LISTBOX
listbox = Listbox(top, width=100, height=15)
listbox.pack(pady=20)

# LOAD ROOMS ON START
load_rooms()

top.mainloop()
