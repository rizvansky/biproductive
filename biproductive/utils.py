import datetime


def last_n_days(n: int):
    today = datetime.datetime.today()
    dates = []
    for i in range(n):
        delta = datetime.timedelta(days=n - 1 - i)
        day = (today - delta).date()
        dates.append(day)
    return dates
