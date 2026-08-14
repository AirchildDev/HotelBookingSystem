import sqlite3


def get_bookings():

    con = sqlite3.connect("hotel.db")
    cur = con.cursor()

    cur.execute("""
        SELECT
            id,
            room_number,
            customer_name,
            check_in,
            check_out,
            username
        FROM bookings
        ORDER BY id DESC
    """)

    rows = cur.fetchall()

    con.close()

    return rows