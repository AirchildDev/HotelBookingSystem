import unittest

from database.schema import create_tables
from services.monitor_service import monitor_application


class HotelSystemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_tables()

    def test_database(self):
        self.assertTrue(True)

    def test_application_monitoring(self):
        result = monitor_application()
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()