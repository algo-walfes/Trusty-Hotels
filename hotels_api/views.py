from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Room, PostImages
from .serializer import RoomSerializer,ImagesSerializer

class allRooms(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class roomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class images(generics.ListCreateAPIView):
# class images(APIView):
    queryset = PostImages.objects.all()
    serializer_class = ImagesSerializer
    
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
        
