import unittest

from services.recovery_service import recover_database


class RecoveryTest(unittest.TestCase):

    def test_database_recovery(self):
        result = recover_database()

        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()