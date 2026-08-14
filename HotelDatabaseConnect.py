import sqlite3

con = sqlite3.connect("hotel.db")
cur = con.cursor()

# USERS
cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    phonenum TEXT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT DEFAULT 'user'
)
''')

# ROOMS
cur.execute('''
CREATE TABLE IF NOT EXISTS rooms(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number TEXT,
    room_type TEXT,
    price REAL,
    status TEXT
)
''')

# BOOKINGS
cur.execute('''
CREATE TABLE IF NOT EXISTS bookings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number INTEGER,
    customer_name TEXT,
    check_in TEXT,
    check_out TEXT,
    username TEXT        
)
''')
print("Username column added successfully")

con.commit()
con.close()