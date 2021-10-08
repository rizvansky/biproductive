from django import forms
from .models import Habit


class AddHabitForm(forms.Form):
    habit_name = forms.CharField(label='Habit name', max_length=100)
