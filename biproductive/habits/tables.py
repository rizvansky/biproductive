from .models import HabitUsage
import django_tables2 as tables
import datetime


class LastWeekHabitUsageTable(tables.Table):
    name = tables.Column()
    day0 = tables.Column()
    day1 = tables.Column()
    day2 = tables.Column()
    day3 = tables.Column()
    day4 = tables.Column()
    day5 = tables.Column()
    day6 = tables.Column()

