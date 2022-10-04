from django.db import models


class SchoolPerson(models.Model):
    name = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    email = models.EmailField()


class University(models.Model):
    name = models.CharField(max_length=20)
    student = models.ForeignKey(SchoolPerson, on_delete=models.CASCADE)


class LevakModel(models.Model):
    book = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
