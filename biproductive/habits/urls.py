from django.urls import path

from . import views

app_name = 'habits'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('tables/', views.last_week_habit_usage)
]