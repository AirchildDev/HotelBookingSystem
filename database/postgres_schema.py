from database.postgres_connection import get_postgres_connection


def create_postgres_tables():

    con = get_postgres_connection()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            fullname TEXT,
            phonenum TEXT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT DEFAULT 'user'
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id SERIAL PRIMARY KEY,
            room_number TEXT,
            room_type TEXT,
            price NUMERIC(10, 2),
            status TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id SERIAL PRIMARY KEY,
            room_number TEXT,
            customer_name TEXT,
            check_in TEXT,
            check_out TEXT,
            username TEXT
        )
    """)

    con.commit()

    cur.close()
    con.close()

    print("PostgreSQL tables created successfully")


if __name__ == "__main__":
    create_postgres_tables()