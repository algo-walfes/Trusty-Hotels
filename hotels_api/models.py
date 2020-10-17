from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Room(models.Model):
    hotel_name = models.ForeignKey('auth.user', on_delete=models.CASCADE, default='auth.user')
    name = models.TextField(max_length=64)
    slug = models.TextField(max_length=64)
    type = models.CharField(max_length=64)
    price = models.IntegerField()
    size = models.IntegerField()
    capacity = models.IntegerField()
    pets = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    description = models.TextField()
    extras = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class PostImages(models.Model):
    post = models.ForeignKey(Room, default=None, related_name='tracks', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.name