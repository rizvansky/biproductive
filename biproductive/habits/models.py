from django.contrib.auth.models import User
from django.db import models


class Habit(models.Model):
    habit_name = models.CharField(max_length=30)
    creation_date = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.habit_name


class HabitUsage(models.Model):
    usage_time = models.DateTimeField()

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.habit} usage: {self.usage_time}"
