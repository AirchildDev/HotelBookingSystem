import sqlite3
import bcrypt

username = input("Enter new admin username: ")
password = input("Enter new admin password: ")

hashed = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

con = sqlite3.connect("hotel.db")
cur = con.cursor()

cur.execute("""
    INSERT INTO users (username, password, role)
    VALUES (?, ?, 'admin')
""", (username, hashed.decode("utf-8")))

con.commit()
con.close()

print("Admin account created successfully")