from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

top = Tk()
top.title("Hotel Admin Dashboard")
top.geometry("900x600")
top.configure(bg="#220f2a")



def reset_all():
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

    if room_no == "" or room_type == "" or price == "" or status == "":
        messagebox.showwarning("Error", "Fill all fields")
        return

    try:
        con = sqlite3.connect("hotel.db")
        cur = con.cursor()

        cur.execute("INSERT INTO rooms(room_number, room_type, price, status) VALUES(?,?,?,?)",
                    (room_no, room_type, price, status))

        con.commit()
        con.close()

        messagebox.showinfo("Success", "Room Added")
        reset_all()
        view_rooms()
    

    except:
        messagebox.showerror("Error", "Room already exists")


# VIEW ROOMS
def view_rooms():
    listbox.delete(0, END)

    con = sqlite3.connect("hotel.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM rooms")
    rows = cur.fetchall()

    con.close()

    if not rows:
        listbox.insert(END, "No rooms found")
        return

    for row in rows:
        display = f"{row[0]} | Room {row[1]} | {row[2]} | ₦{row[3]} | {row[4]}"
        listbox.insert(END, display)


# SELECT FROM LIST
def select_room(event):
    selected = listbox.get(listbox.curselection())
    data = selected.split(" | ")

    entry_room.delete(0, END)
    entry_room.insert(0, data[1].replace("Room ", ""))

    combo_type.set(data[2])

    entry_price.delete(0, END)
    entry_price.insert(0, data[3].replace("₦", ""))

    combo_status.set(data[4])



# UPDATE ROOM
def update_room():
    try:
        selected = listbox.get(listbox.curselection())
        room_id = selected.split(" | ")[0]

        con = sqlite3.connect("hotel.db")
        cur = con.cursor()

        cur.execute("""
        UPDATE rooms
        SET room_number=?, room_type=?, price=?, status=?
        WHERE id=?
        """, (
            entry_room.get(),
            combo_type.get(),
            entry_price.get(),
            combo_status.get(),
            room_id
        ))

        con.commit()
        con.close()

        messagebox.showinfo("Success", "Room Updated")

        reset_all()
        view_rooms()

    except:
        messagebox.showerror("Error", "Select a room first")

# DELETE ROOM
def delete_room():
    try:
        selected = listbox.get(listbox.curselection())
        room_id = selected.split(" | ")[0]

        con = sqlite3.connect("hotel.db")
        cur = con.cursor()

        cur.execute("DELETE FROM rooms WHERE id=?", (room_id,))
        con.commit()
        con.close()

        messagebox.showinfo("Deleted", "Room Deleted")

        reset_all()
        view_rooms()

    except:
        messagebox.showerror("Error", "Select a room first")


#  USER INTERFACE

title = Label(top, text="HOTEL ADMIN DASHBOARD", font=("verdana", 20, "bold"),
              fg="white", bg="#0f172a")
title.pack(pady=10)

frame = Frame(top, bg="#7e0db3")
frame.pack(pady=10)

# ROOM NUMBER
Label(frame, text="Room No", fg="white", bg="#0f172a").grid(row=0, column=0, pady= 10)
entry_room = Entry(frame)
entry_room.grid(row=0, column=1)

# ROOM TYPE
Label(frame, text="Room Type", fg="white", bg="#0f172a").grid(row=1, column=0, pady= 10)
combo_type = ttk.Combobox(frame, values=["Standard", "Deluxe", "Suite"])
combo_type.grid(row=1, column=1)

# PRICE
Label(frame, text="Price", fg="white", bg="#0f172a").grid(row=2, column=0, pady= 10)
entry_price = Entry(frame)
entry_price.grid(row=2, column=1)

# STATUS
Label(frame, text="Status", fg="white", bg="#0f172a").grid(row=3, column=0, pady= 10)
combo_status = ttk.Combobox(frame, values=["Available", "Booked"])
combo_status.grid(row=3, column=1)

# BUTTONS
btn_frame = Frame(top, bg="#0f172a")
btn_frame.pack(pady=10)

Button(btn_frame, text="Add Room", width=15, command=add_room).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Update Room", width=15, command=update_room).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Delete Room", width=15, command=delete_room).grid(row=0, column=2, padx=5)
Button(btn_frame, text="View Rooms", width= 15, command=view_rooms).grid(row=0, column=3, padx=5)

# LISTBOX
listbox = Listbox(top, width=100, height=15)
listbox.pack(pady=20)

listbox.bind("<<ListboxSelect>>", select_room)

# LOAD DATA
view_rooms()

top.mainloop()
