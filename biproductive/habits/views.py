from django.shortcuts import render
from django.views import generic
from django_tables2 import SingleTableView

from .models import Habit, HabitUsage
from .tables import HabitUsageTable


class IndexView(generic.ListView):
    template_name = 'habits/index.html'

    def get_queryset(self):
        return Habit.objects.all()


class HabitUsageListView(SingleTableView):
    model = HabitUsage
    table_class = HabitUsageTable
    template_name = 'habits/habit_usage_table.html'

