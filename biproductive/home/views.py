from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from habits.models import Habit
from habits.scripts import load_last_week_habit_usage

# Create your views here.


@login_required(login_url="login")
def home_view(request):
    habits = Habit.objects.filter(user=request.user)
    week_usage = load_last_week_habit_usage(habits)
    return render(request=request, template_name="home.html", context={'table': week_usage})
