from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Habit


class IndexView(generic.ListView):
    template_name = "habits/index.html"

    def get_queryset(self):
        return Habit.objects.all()


@csrf_exempt
@login_required(login_url="login")
def add_habit(request):
    if request.method == "GET":
        return render(request, "habits/add_habit.html", status=200)
    elif request.method == "POST":
        habit_name = request.POST["habit_name"]
        user = request.user
        habit = Habit(user=user, habit_name=habit_name, creation_date=datetime.now())
        habit.save()
        return JsonResponse({}, status=200)
