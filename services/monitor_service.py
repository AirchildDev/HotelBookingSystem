import sqlite3
from logger import logger
from services.recovery_service import recover_database

def check_database():

    try:
        con = sqlite3.connect("hotel.db")
        con.execute("SELECT 1")
        con.close()

        logger.info("Database monitoring: OK")
        return True

    except Exception as error:

        logger.error(
            f"Database monitoring: FAILED - {error}"
        )

        return False


def check_rooms():

    try:
        con = sqlite3.connect("hotel.db")
        cur = con.cursor()

        cur.execute("SELECT COUNT(*) FROM rooms")
        cur.fetchone()

        con.close()

        logger.info("Room service monitoring: OK")
        return True

    except Exception as error:

        logger.error(
            f"Room service monitoring: FAILED - {error}"
        )

        return False


def check_bookings():

    try:
        con = sqlite3.connect("hotel.db")
        cur = con.cursor()

        cur.execute("SELECT COUNT(*) FROM bookings")
        cur.fetchone()

        con.close()

        logger.info("Booking service monitoring: OK")
        return True

    except Exception as error:

        logger.error(
            f"Booking service monitoring: FAILED - {error}"
        )

        return False


def monitor_application():

    logger.info("Application monitoring started")

    database = check_database()
    rooms = check_rooms()
    bookings = check_bookings()

    if database and rooms and bookings:

        logger.info(
            "Application monitoring: ALL SYSTEMS OK"
        )

        return True

    logger.warning(
        "Application monitoring: SYSTEM CHECK FAILED"
    )

    logger.info(
        "Automatic recovery started"
    )

    recovery = recover_database()

    if not recovery:

        logger.error(
            "Automatic recovery failed"
        )

        return False

    logger.info(
        "Automatic recovery completed"
    )

    # VERIFY SYSTEM AFTER RECOVERY

    logger.info(
        "Verifying system after recovery"
    )

    database = check_database()
    rooms = check_rooms()
    bookings = check_bookings()

    if database and rooms and bookings:

        logger.info(
            "System recovery verification: SUCCESS"
        )

        return True

    logger.error(
        "System recovery verification: FAILED"
    )

    return False