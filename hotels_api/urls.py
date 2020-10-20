from django.contrib import admin 
from django.urls import path

from .views import allRooms,roomDetail, Favs

urlpatterns = [
    path('',allRooms.as_view(), name = 'all_rooms'),
    path('fav',Favs.as_view(), name = 'favorites'),
    # path('images',images.as_view(), name = 'rooms_images'),
    path('<int:pk>', roomDetail.as_view(), name = 'room_details'),
]