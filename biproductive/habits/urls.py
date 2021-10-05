from django.urls import path

from . import views

app_name = "habits"
urlpatterns = [
    path("add_habit/", views.add_habit, name="add_habit"),
]
