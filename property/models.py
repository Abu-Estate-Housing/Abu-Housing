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

# class Status(models.Model):
#     status  = models.CharField(max_length=20, unique=True, null=False)
#     created_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.status}"

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
    AVAILABLE = "available"
    NOT_AVAILABLE = "not_available"
    STATUS_CHOICE = (
        (AVAILABLE, AVAILABLE),
        (NOT_AVAILABLE, NOT_AVAILABLE),
    )
    tenant = models.ForeignKey(
        User, null=True, blank=True, related_name="tenant_properties", on_delete=models.DO_NOTHING
    )
    landlord = models.ForeignKey(
        Landlord, null=True, blank=True, related_name="landlord_properties", on_delete=models.DO_NOTHING
    )
    property_type = models.ForeignKey(Type, null =False, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, null=False, default=NOT_AVAILABLE)
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


    @property
    def photos(self):
        photos = self.photo_set.all()
        photos_format = format_html("")
        for photo in photos:
            print(f'urls for photo {photo.image.url}')
            photos_format += format_html(
                '<img src="{}" width="{}" height="{}" /><p></p><p></p>',
                photo.image.url, 300, 200
            )
        
        return photos_format
    def __str__(self):
        return f"{self.tenant} Propety {self.street}"


class Photo(models.Model):
    image = models.ImageField(upload_to="properties/images", null=False)
    property_name = models.ForeignKey(Property, null=False, on_delete=models.CASCADE)
