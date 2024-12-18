import unittest
from utc_validator import is_valid_utc_time

class TestFindUTCTimes(unittest.TestCase):

    def test_valid_utc_times(self):
        # Тест на корректные строки
        self.assertTrue(is_valid_utc_time("2024-12-18T14:30:45Z"))
        self.assertTrue(is_valid_utc_time("2024-12-18T23:59:59+03:00"))

    def test_invalid_utc_times(self):
        # Тест на некорректные строки
        self.assertFalse(is_valid_utc_time("invalid_time_string"))
        self.assertFalse(is_valid_utc_time("2024-12-18T25:00:00Z"))
        self.assertFalse(is_valid_utc_time("2024-12-18T12:60:00Z"))

    def test_mixed_valid_and_invalid_times(self):
        # Тест на смешанные корректные и некорректные строки
        self.assertTrue(is_valid_utc_time("2024-12-18T14:30:45Z"))
        self.assertTrue(is_valid_utc_time("2024-12-18T23:59:59+03:00"))
        self.assertFalse(is_valid_utc_time("invalid"))
        self.assertFalse(is_valid_utc_time("2024-12-18T25:00:00Z"))

if __name__ == "__main__":
    unittest.main()