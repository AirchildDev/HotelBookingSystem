import sqlite3

con = sqlite3.connect("hotel.db")
cur = con.cursor()

cur.execute("DELETE FROM rooms WHERE id = ?", (10,))

con.commit()
con.close()

print("Duplicate room deleted successfully.")