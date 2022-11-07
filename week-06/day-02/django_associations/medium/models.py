from django.db import models

class User(models.Model):
    pass

class Post(models.Model):
    author = models.ForeignKey(User, models.CASCADE, related_name="posts")

class Comment(models.Model):
    author = models.ForeignKey(User, models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, models.CASCADE, related_name="comments")