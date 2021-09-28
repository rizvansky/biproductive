from django.urls import path

from .views import login_view, logout_view, signup

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("login", login_view, name="login"),
]
