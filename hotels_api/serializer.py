from rest_framework import serializers

from .models import Room, PostImages
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = '__all__'
        # depth = 1
        
class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['hotel_name','name','slug','type','price','size','capacity','pets','breakfast','featured','description','extras','published_at', 'tracks']
        depth = 1
