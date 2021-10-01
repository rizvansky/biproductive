from django.urls import path

from . import views

app_name = 'productivity'
urlpatterns = [
    path('', views.productivity),
]