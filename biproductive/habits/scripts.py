import datetime
from .models import Habit


def last_week_days(today: datetime.datetime):
    dates = []
    for i in range(7):
        delta = datetime.timedelta(days=6-i)
        day = (today - delta).date()
        dates.append(day)
    return dates


def load_last_week_habit_usage():
    today = datetime.datetime.today()
    days = last_week_days(today)
    data = []
    for habit in Habit.objects.all():
        row = {'name': habit.habit_name}
        for i, day in enumerate(days):
            if habit.habitusage_set.filter(usage_time__date=day):
                row[f'day{i}'] = '+'
            else:
                row[f'day{i}'] = '-'
        data.append(row)
    return data
