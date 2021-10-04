import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
data = [
    {
        "date": "04.10.2021",
        "Drinking tea": "yes",
        "Smoking": "no",
        "Making startup": "yes",
        "Drinking beer": "yes",
    },
    {
        "date": "05.10.2021",
        "Drinking tea": "no",
        "Smoking": "yes",
        "Making startup": "yes",
        "Drinking beer": "yes",
    },
]


@login_required(login_url="login")
def home_view(request):
    return render(
        request=request,
        template_name="home.html",
        context={
            "brain_chart": json.dumps(
                {
                    "date": [
                        "04.10.2021",
                        "05.10.2021",
                        "06.10.2021",
                        "07.10.2021",
                        "08.10.2021",
                        "09.10.2021",
                    ],
                    "brain-activity": [10, 20, 25, 30, 60, 50],
                }
            ),
            "habit_table_data": json.dumps(data),
            "habit_names": list(data[0].keys()),
        },
    )
