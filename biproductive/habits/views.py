from django.shortcuts import render
from django.views import generic
import django_tables2 as tables
from .models import Habit
from .scripts import load_last_week_habit_usage
from .tables import LastWeekHabitUsageTable


class IndexView(generic.ListView):
    template_name = 'habits/index.html'

    def get_queryset(self):
        return Habit.objects.all()

