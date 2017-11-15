from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from verwalten.models import User


class Rechnung(models.Model):
    author = models.ForeignKey('auth.User')
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    leistung = models.CharField(max_length=200)
    betrag = models.FloatField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.leistung
