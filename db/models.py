import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class User(models.Model):
    name = models.CharField(max_length=50, default="Dan")

    def __str__(self):
        return self.name


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=50, default="")
    phoneNumber = models.CharField(max_length=12, default="")


    def __str__(self):
        return self.fullName


class Master(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    skills = models.CharField(max_length=255, default="")
    login = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=30, default="")


    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=20, default="")
    model = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.brand


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=10, default="")
    description = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=20, default="")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)

    def __str__(self):
        return self.description