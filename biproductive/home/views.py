import json
import datetime
from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from productivity.scripts import load_last_n_days_productivity_checks, add_productivity_specified_day
from habits.scripts import load_last_n_days_habit_usage, track_habits_specified_day

from .scripts import correlation


@login_required(login_url="login")
def home_view(request):
    # track_habits_specified_day(request.user, datetime.date.today() - datetime.timedelta(5), '-+ ')
    # add_productivity_specified_day(request.user, datetime.date.today() - datetime.timedelta(5), 50)
    # correlation(request.user)
    week_habit_usage = load_last_n_days_habit_usage(request.user, n=7)
    week_productivity = load_last_n_days_productivity_checks(request.user, n=7)
    return render(
        request=request,
        template_name="home.html",
        context={
            "brain_chart": json.dumps(week_productivity),
            "habit_table_data": json.dumps(week_habit_usage),
            "habit_names": list(week_habit_usage[0].keys()),
            # Do not touch this - this json it passed to datatables.js for correctly rendering in order name of columns
            "datatables_js_cols": json.dumps(
                {"cols": list(week_habit_usage[0].keys())}
            ),
        },
    )
