import json
from datetime import date

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import ProductivityCheck


@csrf_exempt
@login_required(login_url="login")
def productivity(request):
    if request.method == "GET":
        checks = ProductivityCheck.objects.filter(date=date.today(), user=request.user)
        permission = len(checks) == 0
        if permission:
            return render(request, "game.html", {"permission": permission}, status=200)

        else:
            return render(
                request,
                "index.html",
                {"message": "You have completed the test today, come back tomorrow"},
                status=403,
            )
    elif request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        score = int(post_data["prod_score"])
        user = request.user
        check = ProductivityCheck(
            user=user, productivity_value=score, date=date.today()
        )
        check.save()
        return JsonResponse({}, status=200)
