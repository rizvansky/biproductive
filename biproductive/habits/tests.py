import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestProductivityGame(TestCase):
    def setUp(self) -> None:
        self.username = "testUser"
        self.email = "testUser"
        self.password = "+AV/*~K4u3k^5HC"

        self.user = User.objects.create_user(
            username=self.username, email=self.email, password=self.password
        )
        self.user.save()

    def test_can_track_table(self):
        self.assertTrue(
            self.client.login(username=self.username, password=self.password),
            "login failed",
        )
        response = self.client.get(path=reverse("habits:add_habit"), data={"habit_name": "test_habit1"})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(path=reverse("habits:add_habit"), data={"habit_name": "test_habit2"})
        self.assertEqual(response.status_code, 200)
        table = self.client.get(path=reverse("habits:habit_table"), data={})
        correct_table = json.dumps(
            {
                "table": {
                    "test_habit1": ["-", "-", "-", "-", "-", "-", "-"],
                    "test_habit2": ["-", "-", "-", "-", "-", "-", "-"],
                }
            }
        )
