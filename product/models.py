from django.db import models

class Categroy (models.Model):
    name = models.CharField(max_length=100)


class Brand (models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    