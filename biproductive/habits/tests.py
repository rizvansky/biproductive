from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .scripts import load_last_week_habit_usage


class TestHabitTable(TestCase):
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
        response = self.client.post(
            path=reverse("habits:add_habit"), data={"habit_name": "test_habit1"}
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            path=reverse("habits:add_habit"), data={"habit_name": "test_habit2"}
        )
        self.assertEqual(response.status_code, 200)
        table = load_last_week_habit_usage(self.user)
        self.assertEqual(len(table), 7)
        self.assertEqual(len(list(table[0].keys())), 3)
