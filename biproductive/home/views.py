from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json

from habits.scripts import load_last_week_habit_usage
from productivity.scripts import load_last_week_productivity_checks


@login_required(login_url="login")
def home_view(request):
    week_habit_usage = load_last_week_habit_usage(request.user)
    week_productivity = load_last_week_productivity_checks(request.user)
    return render(
        request=request,
        template_name="home.html",
        context={
            'brain-chart': json.dumps(week_productivity),
            'habit_table_data': json.dumps(week_habit_usage),
            'habit_names': list(week_habit_usage[0].keys()),
        })
