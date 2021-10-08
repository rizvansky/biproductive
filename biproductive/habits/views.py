from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import AddHabitForm
from .models import Habit


@csrf_exempt
@login_required(login_url="login")
def add_habit(request):
    if request.method == "POST":
        form = AddHabitForm(request.POST)
        if form.is_valid():
            habit_name = form.cleaned_data["habit_name"]
            habit = Habit(
                habit_name=habit_name, user=request.user, creation_date=datetime.now()
            )
            habit.save()
            return redirect("home")
        else:
            return render(request, "add_habit.html", context={"form": form}, status=401)
    else:
        form = AddHabitForm()
    return render(request, "add_habit.html", {"form": form}, status=200)
