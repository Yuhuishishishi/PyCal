import datetime
from datetime import timedelta
import json
import os.path
from HolidayParser import FixedHoliday, FloatingHoliday



class PyCal:
    """PyCal instance"""
    def __init__(self, country="US"):
        self.country = country
        self.holiday_list = self.read_from_file()

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

        # deviate date1 to the nearest sunday
        first_sun_after_date1 = date1 + timedelta(7 - d1)
        # deviate date2 to the nearest pasising Monday
        last_mon_before_date2 = date2 - timedelta(d2 - 1)

        # compute the number of weeks between first_sun_after_date1 and last_mon_before_date2
        delta = last_mon_before_date2 - first_sun_after_date1
        num_weeks = delta.days / 7
        num_weekdays = num_weeks * 5
        num_weekdays += 7 - d1
        num_weekdays += d2 - 1
        return num_weekdays - 1

