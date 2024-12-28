from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.IntegerField()


class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    email = models.EmailField()
    number = models.IntegerField(max_length=8)