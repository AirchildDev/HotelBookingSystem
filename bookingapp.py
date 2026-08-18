from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from database.connection import get_connection
import session
from logger import logger


def booking_page(parent):

    booking_frame = Frame(
        parent,
        bg="#0b132b"
    )

    # LOAD ROOMS

    def load_rooms():

        combo_room["values"] = []

        check_in = cal_in.get_date()
        check_out = cal_out.get_date()

        con = None
        cur = None

        try:

            con = get_connection()
            cur = con.cursor()

            cur.execute("""
                SELECT room_number, room_type, price
                FROM rooms
                ORDER BY room_number
            """)

            rooms = cur.fetchall()

            room_list = []

            for room in rooms:

                room_number = room[0]
                room_type = room[1]
                price = room[2]

                available = is_room_available(
                    room_number,
                    str(check_in),
                    str(check_out)
                )

                if available:

                    display_text = (
                        f"Room {room_number} - "
                        f"{room_type} - "
                        f"₦{price} - AVAILABLE"
                    )

                else:

                    display_text = (
                        f"Room {room_number} - "
                        f"{room_type} - "
                        f"₦{price} - BOOKED"
                    )

                room_list.append(display_text)

            combo_room["values"] = room_list

        except Exception as error:

            logger.error(
                f"Failed to load rooms: {error}"
            )

            messagebox.showerror(
                "Database Error",
                f"Could not load rooms:\n{error}"
            )

        finally:

            if cur:
                cur.close()

            if con:
                con.close()

    # CHECK ROOM AVAILABILITY

    def is_room_available(
        room,
        check_in,
        check_out
    ):

        con = None
        cur = None

        try:

            con = get_connection()
            cur = con.cursor()

            cur.execute("""
                SELECT id
                FROM bookings
                WHERE room_number = %s
                AND NOT (
                    check_out <= %s
                    OR check_in >= %s
                )
            """, (
                room,
                check_in,
                check_out
            ))

            result = cur.fetchone()

            return result is None

        except Exception as error:

            logger.error(
                f"Room availability check failed: {error}"
            )

            raise

        finally:

            if cur:
                cur.close()

            if con:
                con.close()

    # BOOK ROOM

    def book_room():

        name = entry_name.get().strip()

        selected_room = combo_room.get()

        if name == "" or selected_room == "":

            messagebox.showwarning(
                "Error",
                "Fill all fields"
            )

            return

        room = selected_room.split(" - ")[0].replace(
            "Room ",
            ""
        )

        check_in = cal_in.get_date()
        check_out = cal_out.get_date()

        # CHECK DATE

        if check_in >= check_out:

            logger.warning(
                f"Invalid booking dates: "
                f"User={session.current_user}, "
                f"Check-in={check_in}, "
                f"Check-out={check_out}"
            )

            messagebox.showwarning(
                "Error",
                "Check-out must be after check-in"
            )

            return

        # CHECK ROOM AVAILABILITY

        if not is_room_available(
            room,
            str(check_in),
            str(check_out)
        ):

            logger.warning(
                f"Booking rejected: "
                f"User={session.current_user}, "
                f"Room={room}, "
                f"Check-in={check_in}, "
                f"Check-out={check_out}"
            )

            messagebox.showerror(
                "Error",
                "Room already booked for selected dates"
            )

            return

        # SAVE BOOKING

        con = None
        cur = None

        try:

            con = get_connection()
            cur = con.cursor()

            cur.execute("""
                INSERT INTO bookings(
                    room_number,
                    customer_name,
                    check_in,
                    check_out,
                    username
                )
                VALUES(%s, %s, %s, %s, %s)
            """, (
                room,
                name,
                str(check_in),
                str(check_out),
                session.current_user
            ))

            con.commit()

            logger.info(
                f"Booking created: "
                f"User={session.current_user}, "
                f"Room={room}, "
                f"Check-in={check_in}, "
                f"Check-out={check_out}"
            )

            messagebox.showinfo(
                "Success",
                "Room booked successfully"
            )

            view_bookings()
            load_rooms()

            entry_name.delete(0, END)
            combo_room.set("")

        except Exception as error:

            if con:
                con.rollback()

            logger.error(
                f"Booking failed: "
                f"User={session.current_user}, "
                f"Room={room}, "
                f"Error={error}"
            )

            messagebox.showerror(
                "Error",
                f"Could not complete booking:\n{error}"
            )

        finally:

            if cur:
                cur.close()

            if con:
                con.close()

    # VIEW MY BOOKINGS

    def view_bookings():

        listbox.delete(0, END)

        con = None
        cur = None

        try:

            con = get_connection()
            cur = con.cursor()

            cur.execute("""
                SELECT
                    id,
                    room_number,
                    customer_name,
                    check_in,
                    check_out
                FROM bookings
                WHERE username = %s
                ORDER BY id DESC
            """, (
                session.current_user,
            ))

            rows = cur.fetchall()

            if not rows:

                listbox.insert(
                    END,
                    "You have no bookings yet."
                )

                return

            for row in rows:

                display = (
                    f"{row[0]} | "
                    f"Room {row[1]} | "
                    f"{row[2]} | "
                    f"{row[3]} to {row[4]}"
                )

                listbox.insert(
                    END,
                    display
                )

        except Exception as error:

            logger.error(
                f"Failed to load bookings: {error}"
            )

            messagebox.showerror(
                "Database Error",
                f"Could not load bookings:\n{error}"
            )

        finally:

            if cur:
                cur.close()

            if con:
                con.close()

    # CANCEL BOOKING

    def cancel_booking():

        selected = listbox.curselection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Select a booking first"
            )

            return

        booking = listbox.get(selected[0])

        if "You have no bookings yet" in booking:

            return

        booking_id = booking.split(" | ")[0]

        confirm = messagebox.askyesno(
            "Cancel Booking",
            "Are you sure you want to cancel this booking?"
        )

        if not confirm:

            return

        con = None
        cur = None

        try:

            con = get_connection()
            cur = con.cursor()

            cur.execute("""
                DELETE FROM bookings
                WHERE id = %s
                AND username = %s
            """, (
                booking_id,
                session.current_user
            ))

            con.commit()

            logger.info(
                f"Booking cancelled: "
                f"User={session.current_user}, "
                f"Booking ID={booking_id}"
            )

            messagebox.showinfo(
                "Success",
                "Booking cancelled successfully"
            )

            view_bookings()
            load_rooms()

        except Exception as error:

            if con:
                con.rollback()

            logger.error(
                f"Cancellation failed: "
                f"User={session.current_user}, "
                f"Booking ID={booking_id}, "
                f"Error={error}"
            )

            messagebox.showerror(
                "Error",
                f"Could not cancel booking:\n{error}"
            )

        finally:

            if cur:
                cur.close()

            if con:
                con.close()

    # TITLE

    title = Label(
        booking_frame,
        text="HOTEL RESERVATION SYSTEM",
        font=("verdana", 20, "bold"),
        fg="white",
        bg="#0b132b"
    )

    title.pack(pady=10)

    # FORM FRAME

    frame = Frame(
        booking_frame,
        bg="#0b132b"
    )

    frame.pack(pady=10)

    # CUSTOMER NAME

    Label(
        frame,
        text="Customer Name",
        fg="white",
        bg="#0b132b"
    ).grid(
        row=0,
        column=0,
        pady=10
    )

    entry_name = Entry(
        frame,
        width=30
    )

    entry_name.grid(
        row=0,
        column=1
    )

    # ROOM

    Label(
        frame,
        text="Select Room",
        fg="white",
        bg="#0b132b"
    ).grid(
        row=1,
        column=0,
        pady=10
    )

    combo_room = ttk.Combobox(
        frame,
        width=27
    )

    combo_room.grid(
        row=1,
        column=1
    )

    # CHECK-IN

    Label(
        frame,
        text="Check-In Date",
        fg="white",
        bg="#0b132b"
    ).grid(
        row=2,
        column=0,
        pady=10
    )

    cal_in = DateEntry(
        frame,
        width=27,
        background="darkblue",
        foreground="white"
    )

    cal_in.grid(
        row=2,
        column=1
    )

    # CHECK-OUT

    Label(
        frame,
        text="Check-Out Date",
        fg="white",
        bg="#0b132b"
    ).grid(
        row=3,
        column=0,
        pady=10
    )

    cal_out = DateEntry(
        frame,
        width=27,
        background="darkblue",
        foreground="white"
    )

    cal_out.grid(
        row=3,
        column=1
    )

    # DATE EVENTS

    cal_in.bind(
        "<<DateEntrySelected>>",
        lambda e: load_rooms()
    )

    cal_out.bind(
        "<<DateEntrySelected>>",
        lambda e: load_rooms()
    )

    # BUTTONS

    btn_frame = Frame(
        booking_frame,
        bg="#0b132b"
    )

    btn_frame.pack(pady=10)

    Button(
        btn_frame,
        text="Book Room",
        width=15,
        command=book_room
    ).grid(
        row=0,
        column=0,
        padx=5
    )

    Button(
        btn_frame,
        text="View Bookings",
        width=15,
        command=view_bookings
    ).grid(
        row=0,
        column=1,
        padx=5
    )

    Button(
        btn_frame,
        text="Refresh Rooms",
        width=15,
        command=load_rooms
    ).grid(
        row=0,
        column=2,
        padx=5
    )

    Button(
        btn_frame,
        text="Cancel Booking",
        width=15,
        command=cancel_booking
    ).grid(
        row=0,
        column=3,
        padx=5
    )

    # LISTBOX

    listbox = Listbox(
        booking_frame,
        width=100,
        height=15
    )

    listbox.pack(pady=20)

    # CLEAR BOOKING PAGE

    def clear_bookings():

        entry_name.delete(0, END)
        combo_room.set("")
        listbox.delete(0, END)

    # LOAD AVAILABLE ROOMS

    load_rooms()

    return booking_frame, clear_bookings