from datetime import date

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import ProductivityCheck

@csrf_exempt
@login_required(login_url="login")
def productivity(request: HttpRequest):
    if request.method == "GET":
        checks = ProductivityCheck.objects.filter(date=date.today(), user=request.user)
        permission = len(checks) == 0
        return render(request, 'game.html', {'permission': permission})
    elif request.method == "POST":
        score = int(request.POST['score'])
        user = request.user
        check = ProductivityCheck(user=user, productivity_value=score, date=date.today())
        check.save()
        return redirect('home')



