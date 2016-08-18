import datetime


class Holiday:
    MON,TUE,WED,THU,FRI,SAT,SUN = range(0,7)


    def observe_in_year(self, year):
        pass


class FixedHoliday(Holiday):
    """
    The holidays that are observed on a fixed given day each year
    """
    def __init__(self, month, day, name=""):
        self.month = month
        self.day = day

    def observe_in_year(self, year):
        candidate = datetime.date(year, self.month, self.day)
        # if it's a Sat., the move it to the preceding Friday
        # if it's Sun. then move it to the following Monday
        if candidate.weekday() == 5:
            candidate -= datetime.timedelta(1)
        elif candidate.weekday() == 6:
            candidate += datetime.timedelta(1)
        return candidate


class FloatingHoliday(Holiday):
    """
    The holidays that are floating from year to year
    """

    def __init__(self, ordinal, weekday, month, name=""):
        self.ordinal = ordinal
        self.weekday = weekday
        self.month = month

    def observe_in_year(self, year):
        ordinal = self.ordinal
        # get the first day in the month
        first_day_in_month = datetime.date(day=1, month=self.month, year=year)
        # deviate to the first desired weekday
        if first_day_in_month.weekday()<=self.weekday:
            first_desired_weekday_in_month = first_day_in_month + datetime.timedelta(self.weekday - first_day_in_month.weekday())
        else:
            # to the next week
            first_desired_weekday_in_month = first_day_in_month + datetime.timedelta(weeks=1, days=self.weekday - first_day_in_month.weekday())
            ordinal -= 1

        # plus the ordinal
        candidate = first_desired_weekday_in_month + datetime.timedelta(weeks=max(0, ordinal-1))
        return candidate



