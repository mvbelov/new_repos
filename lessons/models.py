from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    concern = models.ForeignKey('Concern', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} -- {self.model}'


class Concern(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ShopCar(models.Model):
    name = models.CharField(max_length=200)
    concerns = models.ManyToManyField('Concern')

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    email = models.EmailField('email')
    is_show = models.BooleanField('Показывать на странице', default=False)

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class HomeWork(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='image/')
    file = models.FileField(upload_to='files/')


class ModelSlag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    # sl = AutoSlugField()

class MyUser(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
