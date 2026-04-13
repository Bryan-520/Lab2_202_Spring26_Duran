import unittest

from lab2_34 import StockRecord, calculate_weekly_data
import lab2_34

class TestWeeklyAverage(unittest.TestCase):

    def test_weekly_data(self):

        fake_week = [
            lab2_34.StockRecord(open_price=10.0, close_price=20.0, date="Monday"),
            lab2_34.StockRecord(open_price=15.0, close_price=25.0, date="Tuesday"),
            lab2_34.StockRecord(open_price=20.0, close_price=30.0, date="Wednesday"),
        ]

        self.assertEqual(calculate_weekly_data(fake_week), [25.0])

if __name__ == '__main__':
    unittest.main()
