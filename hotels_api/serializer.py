from rest_framework import serializers

from .models import Room, Fav, Comments
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate

# class ImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostImages
#         fields = '__all__'
        # fields = ['images']
        # depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        
class RoomSerializer(serializers.ModelSerializer):
    # tracks = ImagesSerializer('tracks', many=True, read_only=True)
    commentModels = CommentSerializer('commentModels',many = True)
    class Meta:
        model = Room
        fields = ['hotel_name','name','slug','type','price','size','capacity','pets','breakfast','featured','description','extras','published_at','commentModels']
        # fields = '__all__'
        # depth = 1
        # read_only_fields = ('tracks',)

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fav
        fields = '__all__'


