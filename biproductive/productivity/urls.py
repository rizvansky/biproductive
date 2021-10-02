from django.urls import path

from . import views

urlpatterns = [
    path("", views.productivity, name="game"),
]
