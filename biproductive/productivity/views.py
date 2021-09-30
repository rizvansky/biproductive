from datetime import date

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import ProductivityCheck

#@login_required(login_url="login")
def productivity(request: HttpRequest):
    print(request.user.is_authenticated)
    if request.method == "GET":
        checks = ProductivityCheck.objects.filter(date__date=date.today(), user=request.user)
        permission = len(checks) > 0
        return render(request, 'game.html', {'permission': permission})
    elif request.method == "POST":
        pass



