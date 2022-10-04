from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=150, verbose_name='city')

