from django.contrib import admin 
from django.urls import path

from .views import allRooms,roomDetail

urlpatterns = [
    path('',allRooms.as_view(), name = 'all_rooms'),
    path('<int:pk>', roomDetail.as_view(), name = 'room_details'),
]