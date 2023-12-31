from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime
from datetime import date


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    ctreated_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )

    def time_passed (self):
        today = date.today()
        delta = today - self.ctreated_at
        return delta.days