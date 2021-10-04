from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url="login")
def home_view(request):
    return render(request=request, template_name="home.html", context={})
