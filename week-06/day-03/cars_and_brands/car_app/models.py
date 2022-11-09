from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)

class Car(models.Model):
    brand = models.ForeignKey(Brand, models.CASCADE, related_name="cars")
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    color = models.CharField(max_length=255)
    image = models.TextField()