import sqlite3

DATABASE = "hotel.db"


def get_connection():
    return sqlite3.connect(DATABASE)