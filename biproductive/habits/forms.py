from django import forms
from .models import Habit


class AddHabitForm(forms.Form):
    habit_name = forms.CharField(label='Habit name', max_length=100)


class HabitTrackingForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        habits = Habit.objects.filter(user=user)
        for i in range(len(habits)):
            field_name = habits[i].habit_name
            self.fields[field_name] = forms.BooleanField(required=False)