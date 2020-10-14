from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Room(models.Model):
    hotel_name = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    longitude = models.TextField()
    latitude = models.TextField()
    product = models.CharField(max_length=64)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product