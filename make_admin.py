import sqlite3

username = input("Enter username to make admin: ")

con = sqlite3.connect("hotel.db")
cur = con.cursor()

cur.execute("""
UPDATE users
SET role='admin'
WHERE username=?
""", (username,))

con.commit()
con.close()

print("Admin assigned successfully")