from django.shortcuts import render
from django.views import generic

from .models import Habit


class IndexView(generic.ListView):
    template_name = 'habits/index.html'

    def get_queryset(self):
        return Habit.objects.all()
