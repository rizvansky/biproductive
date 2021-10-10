from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import AddHabitForm, HabitTrackingForm
from .models import Habit, HabitUsage


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


@csrf_exempt
@login_required(login_url="login")
def track_habits(request):
    if request.method == 'POST':
        form = HabitTrackingForm(request.user, request.POST)
        if form.is_valid():
            for item in form.cleaned_data.items():
                if item[1] == 'True':
                    habit = Habit.objects.filter(user=request.user, habit_name=item[0])[0]
                    usage = HabitUsage(habit=habit, usage_time=datetime.now(), status=True)
                    usage.save()
                elif item[1] == 'False':
                    habit = Habit.objects.filter(user=request.user, habit_name=item[0])[0]
                    usage = HabitUsage(habit=habit, usage_time=datetime.now(), status=False)
                    usage.save()
            return redirect('home')
        else:
            return render(request, "track_habits.html", context={"form": form}, status=401)
    else:
        form = HabitTrackingForm(request.user)
        return render(request, "track_habits.html", {'form': form}, status=200)
