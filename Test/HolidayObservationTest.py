import unittest
import datetime

class TestHolidayObservation(unittest.TestCase):

	def test_fixed_ob(self):
		
		from PyCal import HolidayParser 

		day = HolidayParser.FixedHoliday(1,1)
		nyd = day.observe_in_year(2016)
		self.assertEqual(nyd, datetime.date(day=1, month=1, year=2016))

	def test_fixed_ob_on_Sun(self):
		from PyCal import HolidayParser

		day = HolidayParser.FixedHoliday(month=7, day=31)
		h = day.observe_in_year(2016)
		self.assertEqual(h, datetime.date(day=1, month=8, year=2016))

	def test_fixed_ob_on_Sat(self):
		from PyCal import HolidayParser

		day = HolidayParser.FixedHoliday(month=7, day=30)
		h = day.observe_in_year(2016)
		self.assertEqual(h, datetime.date(day=29, month=7, year=2016))


if __name__ == '__main__':
	unittest.main()