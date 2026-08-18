from database.connection import get_connection
from logger import logger


def recover_database():

    try:

        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_name = 'users'
        """)

        result = cur.fetchone()

        cur.close()
        con.close()

        if result:

            logger.info(
                "Recovery check: PostgreSQL database is healthy"
            )

            return True

        logger.warning(
            "Recovery check: users table missing"
        )

        return False

    except Exception as error:

        logger.error(
            f"Automatic recovery FAILED: {error}"
        )

        return False