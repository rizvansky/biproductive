import json
from datetime import date
from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from productivity.models import ProductivityCheck


class TestProductivityGame(TestCase):
    def setUp(self) -> None:
        self.username = "testUser"
        self.email = "testUser"
        self.password = "+AV/*~K\4u3k^5HC"

        self.user = User.objects.create_user(
            username=self.username, email=self.email, password=self.password
        )
        self.user.save()

    def test_can_play(self):
        self.assertTrue(
            self.client.login(username=self.username, password=self.password),
            "login failed",
        )
        response = self.client.get(path=reverse("game"), data={})
        self.assertTrue(response.status_code, 200)

    def test_already_played(self):
        productivity = ProductivityCheck.objects.create(
            user=self.user, productivity_value=50, date=date.today()
        )
        productivity.save()

        self.assertTrue(
            self.client.login(username=self.username, password=self.password),
            "login failed",
        )
        response = self.client.get(path=reverse("game"), data={})
        self.assertTrue(response.status_code, 403)

    def test_not_logged_in(self):
        response = self.client.get(path=reverse("game"), data={})
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_can_send_fetch_query(self):
        self.assertTrue(
            self.client.login(username=self.username, password=self.password),
            "login failed",
        )
        json_data = json.dumps({"prod_score": 50})
        response = self.client.generic(
            method="POST", path=reverse("game"), data=json_data
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get(path=reverse("game"), data={})
        self.assertTrue(response.status_code, HTTPStatus.FORBIDDEN)
