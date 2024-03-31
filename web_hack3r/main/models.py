from django.db import models
from django.contrib.auth.models import AbstractUser


def default_data():
    return {"completed_tasks": []}


class CustomUser(AbstractUser):
    user_data = models.JSONField(default=default_data)
    web_points = models.IntegerField('Баллы за веб', default=0)
    reverse_points = models.IntegerField('Баллы за реверс', default=0)
    other_points = models.IntegerField('Баллы за прочее', default=0)
    osint_points = models.IntegerField('Баллы за OSINT', default=0)
    crypto_points = models.IntegerField('Баллы за криптрографию', default=0)
    birth_date = models.DateField('Дата рождения', default='1900-01-01')
