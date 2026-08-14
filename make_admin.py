import sqlite3

con = sqlite3.connect("hotel.db")
cur = con.cursor()

cur.execute("""
UPDATE users
SET role='admin'
WHERE username='komzy'
""")

con.commit()
con.close()

print("Admin assigned successfully")
