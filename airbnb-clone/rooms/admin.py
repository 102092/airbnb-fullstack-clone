from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Room, models.Facility, models.Amenity, models.HouseRule)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    pass


@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
