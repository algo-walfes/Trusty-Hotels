from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Room(models.Model):
    auth = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=64, default=User)
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64,null=True, blank=True)
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
    main_image = models.URLField(blank=True,null=True)
    image1 = models.URLField(blank=True,null=True)
    image2 = models.URLField(blank=True,null=True)
    image3 = models.URLField(blank=True,null=True)
    # comments = models.IntegerField(primary_key=True)
    # this function for add slug auto if it is empty 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Comments(models.Model):
    post = models.ForeignKey(Room,related_name='commentModels', on_delete=models.CASCADE)
    useremail = models.CharField(max_length=64)
    comment = models.TextField()

class Fav(models.Model):
    user_email = models.CharField(max_length=64)
    slug = models.CharField(max_length=64,null=True, blank=True)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    capacity = models.IntegerField()
    size = models.IntegerField()
    price = models.IntegerField()
    extras = models.TextField(blank=True)
    breakfast = models.CharField(max_length=5)
    pets = models.CharField(max_length=5)
    images = models.TextField()
    hotelName = models.CharField(max_length=64)
    published_at = models.CharField(max_length=64)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)

# class PostImages(models.Model):
#     post = models.ForeignKey(Room, default=None, related_name='tracks', on_delete=models.CASCADE, blank=True,null=True)
#     images = models.ImageField(upload_to='images/',blank=True,null=True)

#     def __str__(self):
#         return self.post.name