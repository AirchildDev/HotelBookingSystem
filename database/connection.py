from database.postgres_connection import get_postgres_connection


def get_connection():
    return get_postgres_connection()