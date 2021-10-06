from utils import last_n_days
from .models import Habit


def load_last_n_days_habit_usage(user, n: int):
    habits = Habit.objects.filter(user=user)
    days = last_n_days(n)
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
