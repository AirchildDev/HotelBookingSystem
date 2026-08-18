from database.connection import get_connection
from logger import logger


def create_room(room_number, room_type, price, status):

    try:

        con = get_connection()
        cur = con.cursor()

        # Check if room already exists
        cur.execute(
            "SELECT id FROM rooms WHERE room_number = %s",
            (room_number,)
        )

        if cur.fetchone():

            logger.warning(
                f"Duplicate room attempt: {room_number}"
            )

            cur.close()
            con.close()

            raise ValueError("Room number already exists")

        # Add new room
        cur.execute("""
            INSERT INTO rooms(
                room_number,
                room_type,
                price,
                status
            )
            VALUES (%s, %s, %s, %s)
        """, (
            room_number,
            room_type,
            price,
            status
        ))

        con.commit()

        cur.close()
        con.close()

        logger.info(
            f"Room {room_number} created successfully"
        )

    except Exception as error:

        logger.error(
            f"Failed to create room {room_number}: {error}"
        )

        raise


def get_rooms():

    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        SELECT
            id,
            room_number,
            room_type,
            price,
            status
        FROM rooms
        ORDER BY id
    """)

    rows = cur.fetchall()

    cur.close()
    con.close()

    return rows


def update_room_record(
    room_id,
    room_number,
    room_type,
    price,
    status
):

    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        UPDATE rooms
        SET
            room_number = %s,
            room_type = %s,
            price = %s,
            status = %s
        WHERE id = %s
    """, (
        room_number,
        room_type,
        price,
        status,
        room_id
    ))

    con.commit()

    cur.close()
    con.close()


def delete_room_record(room_id):

    con = get_connection()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM rooms WHERE id = %s",
        (room_id,)
    )

    con.commit()

    cur.close()
    con.close()