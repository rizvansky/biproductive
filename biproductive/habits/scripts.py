import datetime

from .models import Habit


def last_week_days(today: datetime.datetime):
    dates = []
    for i in range(7):
        delta = datetime.timedelta(days=6 - i)
        day = (today - delta).date()
        dates.append(day)
    return dates


def load_last_week_habit_usage(user):
    habits = Habit.objects.filter(user=user)
    today = datetime.datetime.today()
    days = last_week_days(today)
    data = []
    for i, day in enumerate(days):
        row = {"date": f"{day}"}
        for habit in habits:
            if habit.habitusage_set.filter(usage_time__date=day):
                row[f"{habit}"] = "yes"
            else:
                row[f"{habit}"] = "no"
        data.append(row)
    return data
