from django.urls import path

from . import views

app_name = 'habits'
urlpatterns = [
    path('', views.week_habit_usage),
    path('add_habit/', views.add_habit),
]