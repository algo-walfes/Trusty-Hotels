from rest_framework import serializers

from .models import Room
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate

# class ImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostImages
#         fields = '__all__'
        # fields = ['images']
        # depth = 1
        
class RoomSerializer(serializers.ModelSerializer):
    # tracks = ImagesSerializer('tracks', many=True, read_only=True)

    class Meta:
        model = Room
        # fields = ['hotel_name','name','slug','type','price','size','capacity','pets','breakfast','featured','description','extras','published_at']
        fields = '__all__'
        # depth = 1
        # read_only_fields = ('tracks',)
