from django.db import models

# Create your models here.
class ListCars(models.Model):
    nameCat = models.CharField(max_length=255)
    content = models.TextField(default="")
    price = models.PositiveSmallIntegerField(default=1)
    year = models.PositiveSmallIntegerField(default=2000)