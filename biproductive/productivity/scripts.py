import datetime

from .models import ProductivityCheck


def last_week_days(today: datetime.datetime):
    dates = []
    for i in range(7):
        delta = datetime.timedelta(days=6 - i)
        day = (today - delta).date()
        dates.append(day)
    return dates


def load_last_week_productivity_checks(user):
    checks = ProductivityCheck.objects.filter(user=user)
    today = datetime.datetime.today()
    days = last_week_days(today)
    data = {"date": list(map(str, days)), "brain-activity": []}
    for i, day in enumerate(days):
        if checks.filter(date=day):
            data["brain-activity"].append(checks.filter(date=day)[0].productivity_value)
        else:
            data["brain-activity"].append(0)
    return data
