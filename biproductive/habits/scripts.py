import datetime

from utils import last_n_days
from .models import Habit, HabitUsage


def load_last_n_days_habit_usage(user, n: int):
    habits = Habit.objects.filter(user=user)
    days = last_n_days(n)
    data = []
    for day in days:
        row = {"date": f"{day}"}
        for habit in habits:
            if habit.habitusage_set.filter(usage_time__date=day, status=True):
                row[f"{habit}"] = "+"
            elif habit.habitusage_set.filter(usage_time__date=day, status=False):
                row[f"{habit}"] = "-"
            else:
                row[f"{habit}"] = ' '
        data.append(row)
    return data


def track_habits_specified_day(user, day: datetime.date, fill: str):
    habits = Habit.objects.filter(user=user)
    for habit, status in zip(habits, fill):
        if status == ' ':
            continue
        else:
            status = (status == '+')
            usage = HabitUsage(usage_time=day, status=status, habit=habit)
            usage.save()