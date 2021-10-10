# Create your tests here.

from django.contrib.auth.models import User
from django.http import FileResponse
from django.test import TestCase
from django.urls import reverse


class ReportGenerationTestCase(TestCase):
    def setUp(self):
        self.username = "ufaiisluntvia"
        self.password = "kneJe^fBgGR#"

        user = User.objects.create_user(
            username=self.username,
            password=self.password,
            is_active=True
        )
        user.save()
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_report_generation(self):
        response = self.client.post(
            reverse('login'),
            data={'username': self.username, 'password': self.password}
        )

        self.assertEqual(response.url, reverse('home'), 'failed to login')

        response = self.client.get(reverse('report'))
        self.assertTrue(type(response) == FileResponse)
