from django.db import models

class User(models.Model):
    pass

class Restaurant(models.Model):
    pass

class FoodItem(models.Model):
    pass

class Order(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name="orders")
    restaurant = models.ForeignKey(Restaurant, models.CASCADE, related_name="orders")
    food_items = models.ManyToManyField(FoodItem, through="OrderFoodItem", related_name="orders")

class OrderFoodItem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE, related_name="order_food_items")
    food_item = models.ForeignKey(FoodItem, models.CASCADE, related_name="order_food_items")
