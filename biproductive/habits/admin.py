from django.contrib import admin
from .models import Habit, HabitUsage


admin.site.register(Habit)
admin.site.register(HabitUsage)
