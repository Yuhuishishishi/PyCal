import unittest
from datetime import date

class HolidayReaderTest(unittest.TestCase):

	def test_reader_size(self):
		from PyCal import BusCal

		cal = BusCal.PyCal()
		self.assertEqual(len(cal.holiday_list),8)


	def test_2016_observance(self):
		from PyCal import BusCal

		cal = BusCal.PyCal()
		for d in cal.holiday_list:
			ob = d.observe_in_year(2016)
			if d.name=="New Year's Day":
				real = date(year=2016,month=1,day=1)
			elif d.name=="Independence Day":
				real = date(year=2016,month=7,day=4)
			elif d.name=="Veterans Day":
				real = date(year=2016,month=11,day=11)
			elif d.name=="Christmas Day":
				real = date(year=2016,month=12,day=26)
			elif d.name=="MLK":
				real = date(year=2016,month=1,day=18)
			elif d.name=="Memorial Day":
				real = date(year=2016,month=5,day=30)
			elif d.name=="Labor Day":
				real = date(year=2016,month=9,day=5)
			elif d.name=="Columbus Day":
				real = date(year=2016,month=10,day=10)

			self.assertEqual(ob, real)


if __name__ == '__main__':
	unittest.main()