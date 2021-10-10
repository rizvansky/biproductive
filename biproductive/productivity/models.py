from django.contrib.auth.models import User
from django.db import models


class ProductivityCheck(models.Model):
    date = models.DateField()
    productivity_value = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Productivity check: User:{self.user}, " \
               f"Date:{self.date}, Value:{self.productivity_value}"
