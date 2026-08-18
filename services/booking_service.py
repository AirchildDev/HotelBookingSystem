from database.connection import get_connection


def get_bookings():

    con = get_connection()
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

    cur.close()
    con.close()

    return rows