import datetime
from datetime import timedelta
from collections import defaultdict
import json
import os.path
from HolidayParser import FixedHoliday, FloatingHoliday



class PyCal:
    """PyCal instance"""
    def __init__(self, country="US"):
        self.country = country
        self.holiday_list = self.read_from_file()
        self._holiday_hash_table()

    def read_from_file(self):
        parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(parent_path, ".".join([self.country.lower(), "holiday"]))

        result = []
        with open(file_path) as fp:
            j = json.load(fp)
            holiday_list = j["holidays"]
            for d in holiday_list:
                if d["type"]=="fixed":
                    new_day = FixedHoliday(month=d["month"], day=d["day"],
                        name=d["name"])
                else:
                    new_day = FloatingHoliday(month=d["month"], weekday=d["weekday"],
                        ordinal=d["ordinal"], name=d["name"])
                result.append(new_day)

        return result

    def _holiday_hash_table(self):
        holiday_hash = defaultdict(list)
        for day in self.holiday_list:
            holiday_hash[day.month].append(day)

        return holiday_hash


    def week_days_between(self, date1, date2):
        """
        get the number of weekdays (excluding Sat. and Sun.) between two dates
        :param date1: datetime.date
        :param date2: datetime.date
        :return: number of week days between date1 and date2
        """
        if date1 == date2:
            return 0
        elif date1 > date2:
            # swap date1 and date2 so that date1 is always before date2
            date1, date2 = date2, date1

        # check if they are within the same week
        y1, w1, d1 = date1.isocalendar()
        y2, w2, d2 = date2.isocalendar()
        if y1 == y2 and w1 == w2:
            return d2 - d1

        num_weekdays = 0

        entire_weeks_in_between = w2-w1-1
        num_weekdays += entire_weeks_in_between*5

        remaining_weekdays_from_date1 = max(6-d1,0) 
        passed_weekdays_to_date2 = min(6,d2) - 1

        num_weekdays += remaining_weekdays_from_date1
        num_weekdays += passed_weekdays_to_date2

        # subtract the observed holidays
        num_weekdays -= self._holidays_between(date1, date2)

        return num_weekdays 

    def _holidays_between(self, date1, date2):
        num_holidays = 0
        # if two dates in the same year
        # assume date1 < date2

        # date1 and date2 in the same year
        if date2.year-date1.year == 0:
            holidays_between = [day for day in self.holiday_list if day.observe_in_year(date1.year) >= date1 and day.observe_in_year(date1.year) <= date2]
            return len(holidays_between)

        if date2.year-date1.year > 1:
            num_entire_years = date2.year-date1.year
            num_holidays += num_entire_years*len(self.holiday_list)

        # holidays from date1 to the end of year
        remaining_holiday_from_date1 = [day for day in self.holiday_list if day.observe_in_year(date1.year) >= date1]

        # holidays from the start pf year to date2
        passed_holiday_to_date2 = [day for day in self.holiday_list if day.observe_in_year(date2.year) <= date2]

        num_holidays += len(remaining_holiday_from_date1)
        num_holidays += len(passed_holiday_to_date2)

        return num_holidays