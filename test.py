import sqlite3

con = sqlite3.connect("hotel.db")
cur = con.cursor()

cur.execute("SELECT username, role FROM users")

print(cur.fetchall())

con.close()
