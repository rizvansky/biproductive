import datetime

from utils import last_n_days

from .models import ProductivityCheck


def load_last_n_days_productivity_checks(user, n: int):
    checks = ProductivityCheck.objects.filter(user=user)
    days = last_n_days(n)
    data = {"date": list(map(str, days)), "brain-activity": []}
    for day in days:
        if checks.filter(date=day):
            data["brain-activity"].append(checks.filter(date=day)[0].productivity_value)
        else:
            data["brain-activity"].append(0)
    return data


def add_productivity_specified_day(user, day: datetime.date, value: int):
    if ProductivityCheck.objects.filter(user=user, date=day):
        check: ProductivityCheck = ProductivityCheck.objects.get(user=user, date=day)
        check.productivity_value = value
        check.save()
    else:
        check = ProductivityCheck(user=user, date=day, productivity_value=value)
        check.save()
