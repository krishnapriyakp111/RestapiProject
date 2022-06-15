from django.db import models
from django.contrib.auth.models import User


# Creating models here.
class emp_details(models.Model):
    name = models.CharField(max_length = 100)
    latitude = models.FloatField(max_length=90)
    longitude = models.FloatField(max_length=180)
    def __str__(self):
        return self.name
