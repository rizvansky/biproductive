from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm


@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # load the profile instance created by the signal
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("home")

        else:
            return render(request, "signup.html", context={"form": form}, status=401)
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form}, status=200)


@login_required(login_url="login")
@csrf_exempt
def logout_view(request):
    username = "No idea"
    if request.user.is_authenticated:
        username = request.user.username

    logout(request)

    return render(
        request,
        "index.html",
        context={"message": f"{username} has logged out!"},
        status=200,
    )


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        # print(f"cleaned data: {form.cleaned_data}")
        if form.is_valid():

            data = form.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(
                    request,
                    "login.html",
                    {
                        "form": AuthenticationForm(),
                        "message": "Invalid login",
                    },
                    status=401,
                )
        else:
            return render(
                request,
                "login.html",
                {"form": AuthenticationForm()},
                status=401,
            )

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})
