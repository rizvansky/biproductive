from utils import last_n_days
from .models import ProductivityCheck


def load_last_n_days_productivity_checks(user, n: int):
    checks = ProductivityCheck.objects.filter(user=user)
    days = last_n_days(n)
    data = {"date": list(map(str, days)), "brain-activity": []}
    for i, day in enumerate(days):
        if checks.filter(date=day):
            data["brain-activity"].append(checks.filter(date=day)[0].productivity_value)
        else:
            data["brain-activity"].append(0)
    return data
