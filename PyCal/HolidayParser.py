import datetime


class Holiday:
    def observe_in_year(self, year):
        pass


class FixedHoliday(Holiday):
    """
    The holidays that are observed on a fixed given day each year
    """

    def __init__(self, month, day):
        self.month = month
        self.day = day

    def observe_in_year(self, year):
        return datetime.date(year, self.month, self.day)


class FirstDayOfSomethingHoliday(Holiday):
    def __init__(self, weekday, month, order):
        self.weekday = weekday
        self.month = month
        self.order = order

    def observe_in_year(self, year):
        # first day in the month
        first_day_of_month = datetime.date(year, self.month, 1)
