from django.db import models

class User(models.Model):
    pass

class Shop(models.Model):
    owner = models.OneToOneField(User, models.CASCADE, related_name="shop")

class Product(models.Model):
    shop = models.ForeignKey(Shop, models.CASCADE, related_name="products")

class Review(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, models.CASCADE, related_name="reviewed_products")