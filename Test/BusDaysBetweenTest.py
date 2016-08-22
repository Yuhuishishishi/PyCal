import unittest
from datetime import date

class BusDaysBetweenTest(unittest.TestCase):

	def test_same_year_date(self):
		date1 = date(year=2016, month=1, day=11)
		date2 = date(year=2016, month=1, day=22)

		from PyCal import BusCal

		cal = BusCal.PyCal()
		b_days_between = cal.week_days_between(date1, date2)
		self.assertEqual(b_days_between, 8)


if __name__ == '__main__':
	unittest.main()
