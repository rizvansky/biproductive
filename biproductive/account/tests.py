# Create your tests here.
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegisterTestCase(TestCase):
    def setUp(self) -> None:
        self.email = "ufai@isluntvia.com"
        self.username = "ufaiisluntvia"
        self.password = "kneJe^fBgGR#"

    def test_can_register(self) -> None:
        response = self.client.post(
            reverse("signup"),
            data={
                "email": self.email,
                "username": self.username,
                "password1": self.password,
                "password2": self.password,
            },
        )

        self.assertEqual(response.status_code, 200)

        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_can_not_register_if_username_exists(self):
        User.objects.create(
            username=self.username, email=self.email, password=self.password
        )

        response = self.client.post(
            reverse("signup"),
            data={
                "email": self.email,
                "username": self.username,
                "password1": self.password,
                "password2": self.password,
            },
        )

        self.assertEqual(response.status_code, 401)

        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)


class LoginTestCase(TestCase):
    def setUp(self) -> None:
        self.username = "ufaiisluntvia"
        self.password = "kneJe^fBgGR#"

        User.objects.create(username=self.username, password=self.password)
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_can_login(self) -> None:
        response = self.client.post(
            reverse("login"),
            data={"username": self.username, "password": self.password},
        )

        self.assertEqual(response.status_code, 200)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_can_not_login_with_invalid_username(self):
        response = self.client.post(
            reverse("login"),
            data={"username": "erweirufhuierfhfheiourh", "password": self.password},
        )

        self.assertEqual(response.status_code, 401)

        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_can_not_login_with_invalid_password(self):
        response = self.client.post(
            reverse("login"),
            data={"username": self.username, "password": "K\a&~jY2cdAEXks"},
        )

        self.assertEqual(response.status_code, 401)
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)
