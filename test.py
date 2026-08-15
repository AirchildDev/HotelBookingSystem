import sqlite3
from database.schema import create_tables

# Create database tables
create_tables()

# Connect to database
con = sqlite3.connect("hotel.db")
cur = con.cursor()

# Test users table
cur.execute("SELECT username, role FROM users")

print(cur.fetchall())

con.close()

print("Database test passed!")