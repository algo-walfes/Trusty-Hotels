from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .models import Room
from .serializer import RoomSerializer

class allRooms(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class roomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer