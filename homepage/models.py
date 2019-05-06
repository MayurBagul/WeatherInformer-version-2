from django.db import models


class Data(models.Model):
    temp = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    water = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.city


