import random
import datetime
from rich import print
import matplotlib.dates as mdates

"""
reduce list of many dates to single day time
"""

def datetime_to_unix(date):
    """convert datetime object to unix time"""
    return date.timestamp()
    
    
def random_dates(n):
    """generate random dates from today in range of n
    # base_date = datetime.date.now()
    # base_date = datetime.time.now()
    # base_date = datetime.datetime.now()
    """
    base_date = datetime.datetime.today()
    dates = []
    for x in range(n):
        days = random.randrange(30)
        hours = random.randrange(24)
        minutes = random.randrange(60)
        delta = datetime.timedelta(days=days, hours=hours, minutes=minutes)
        date = base_date + delta
        dates.append(date)
    return dates
    
    
def reduce_dates(dates_list, base_date=None):
    """reduce dates to single day time
    https://stackoverflow.com/questions/8474670/pythonic-way-to-combine-datetime-date-and-datetime-time-objects
    """
    if base_date is None:
        base_date = datetime.datetime.today()
    reduced = [datetime.datetime.combine(base_date, date.time()) for date in dates_list]
    return reduced
    
    
if __name__ == "__main__":
    dates = random_dates(10)
    print(dates)
    reduced = reduce_dates(dates)
    print(reduced)
    