from django.db import models
from django.contrib.auth.models import User

class Campus(models.Model):
    name = models.CharField(max_length=200)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Order(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)