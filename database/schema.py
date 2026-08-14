from database.connection import get_connection


def create_tables():
    con = get_connection()
    cur = con.cursor()

    # USERS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            phonenum TEXT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT DEFAULT 'user'
        )
    """)

    # ROOMS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS rooms(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number TEXT,
            room_type TEXT,
            price REAL,
            status TEXT
        )
    """)

    # BOOKINGS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number INTEGER,
            customer_name TEXT,
            check_in TEXT,
            check_out TEXT,
            username TEXT
        )
    """)

    con.commit()
    con.close()

    print("Database tables created successfully")