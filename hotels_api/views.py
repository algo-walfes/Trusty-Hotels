from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.views import APIView
# from django_filters.rest_framework import DjangoFilterBackend
# from django.contrib.auth.models import User
from .permissions import ReadOnly

# Create your views here.
from .models import Room
from .serializer import RoomSerializer
from django.contrib.auth.models import User


class allRooms(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (ReadOnly,)

    # def create(self, request, *args, **kwargs):
    #     room_data = request.data
    #     user = User.objects.get(id)

    #     new_room = Room.objects.create(hotel_name=user, name=room_data['name'], slug=room_data['slug'], type=room_data['type'], price=room_data['price'], size=room_data['size'], capacity=room_data['capacity'], description=room_data['description'], extras=room_data['extras'])

    #     new_room.save()
    #     serializer = RoomSerializer(new_room)

    #     return Response(serializer.data)


class roomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# class images(generics.ListCreateAPIView):
# # class images(APIView):
#     queryset = PostImages.objects.all()
#     serializer_class = ImagesSerializer
    
    # def get_queryset(self):
    #     cars = PostImages.objects.all()
    #     return cars

    # def get(self, request, *args, **kwargs):
    #     try:
    #         id = request.query_params["id"]
    #         if id != None:
    #             image = PostImages.objects.get(post=id)
    #             serializer = ImagesSerializer(image)
    #     except:
    #         images = self.get_queryset()
    #         serializer = ImagesSerializer(images, many=True)

    #     return Response(serializer.data)
        
