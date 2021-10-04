import json
from datetime import datetime

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Habit

from .scripts import load_last_week_habit_usage


class IndexView(generic.ListView):
    template_name = 'habits/index.html'

    def get_queryset(self):
        return Habit.objects.all()


@csrf_exempt
@login_required(login_url="login")
def add_habit(request):
    if request.method == "GET":
        return render(request, "habits/add_habit.html", status=200)
    elif request.method == "POST":
        habit_name = request.POST['habit_name']
        user = request.user
        habit = Habit(
            user=user, habit_name=habit_name, creation_date=datetime.now()
        )
        habit.save()
        return JsonResponse({}, status=200)


@login_required(login_url="login")
def week_habit_usage(request):
    habits = Habit.objects.filter(user=request.user)
    week_usage = load_last_week_habit_usage(habits)
    return JsonResponse({'table': week_usage}, status=200)

