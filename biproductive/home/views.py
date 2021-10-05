from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from habits.scripts import load_last_week_habit_usage


@login_required(login_url="login")
def home_view(request):
    week_usage = load_last_week_habit_usage(request.user)
    return render(request=request, template_name="home.html", context={'table': week_usage})
