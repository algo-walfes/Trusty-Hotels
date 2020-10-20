from django.contrib import admin
from .models import Room, Fav
# Register your models here.
# class PostImagesAdmin(admin.StackedInline):
#     model = PostImages

# @admin.register(Room)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImagesAdmin]

#     class Meta:
#         model = Room


# @admin.register(PostImages)
# class PostImagesAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Room)
admin.site.register(Fav)