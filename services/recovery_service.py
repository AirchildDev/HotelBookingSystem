from database.connection import get_connection
from database.schema import create_tables
from logger import logger


def recover_database():
    try:
        con = get_connection()
        cur = con.cursor()

        cur.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='users'"
        )

        result = cur.fetchone()

        con.close()

        if result:
            logger.info("Recovery check: Database is healthy")
            return True

        logger.warning(
            "Recovery check: users table missing"
        )

        create_tables()

        logger.info(
            "Automatic recovery: Database tables recreated"
        )

        return True

    except Exception as error:
        logger.error(
            f"Automatic recovery FAILED: {error}"
        )
        return False