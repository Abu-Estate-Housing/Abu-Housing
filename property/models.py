import datetime
from enum import unique
from django.db import models
from django.utils.html import format_html
from user.models import Landlord, User


class Type(models.Model):
    types = models.CharField(max_length=50, unique=True, null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.types}"

class Status(models.Model):
    status  = models.CharField(max_length=20, unique=True, null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.status}"

class Listing(models.Model):
    types = models.CharField(max_length=50, unique=True, null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.types}"

class Amenity(models.Model):
    amenity = models.CharField(max_length=30, null=True, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.amenity}"


class Property(models.Model):
    occupant = models.ForeignKey(
        User, null=True, blank=True, related_name="occupant_properties", on_delete=models.DO_NOTHING
    )
    landlord = models.ForeignKey(
        Landlord, null=True, blank=True, related_name="landlord_properties", on_delete=models.DO_NOTHING
    )
    property_type = models.ForeignKey(Type, null =False, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, null=False, on_delete=models.DO_NOTHING)
    listing = models.ForeignKey(Listing, null=False, on_delete=models.DO_NOTHING)
    price = models.IntegerField(null=True, blank=True)
    bedroom = models.IntegerField(null=True, blank=True)
    bathroom = models.IntegerField(null=True, blank=True)
    amenity = models.ManyToManyField(
        Amenity, related_name="properties", blank=True
    )
    description = models.TextField(null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    latittude = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    created_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    def photos(self):
        photos = self.photo_set.all()
        photos_format = format_html("")
        for photo in photos:
            photos_format += format_html(
                '<img src="{0}" width"{1}" height="{2}" /><p></p>'.format(
                    photo.image.url, 300, 200
                )
            )
        
        return photos_format

    def __str__(self):
        return f"{self.occupant} Propety"


class Photo(models.Model):
    image = models.ImageField(upload_to="properties/images", null=False)
    property_name = models.ForeignKey(Property, null=False, on_delete=models.DO_NOTHING)
