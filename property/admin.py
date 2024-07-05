from django.contrib import admin
from django.utils.html import format_html
from .forms import PropertyAdminForm
from unfold.admin import ModelAdmin

from property.models import Amenity, Listing, Photo, Property, Type

# Register your models here.
#
@admin.register(Property)
class ProprtyAdmin(ModelAdmin):

    form = PropertyAdminForm
    list_filter = ("status", "property_type", "listing")
    search_fields = ('tenant__email',)
    list_display = (
        "tenant", "bedroom", "bathroom", "price_in_naira", "city", "street", "status",
    )
    readonly_fields = ("photos",)

    def price_in_naira(self, obj):
        formatted_price = "₦{:.2f}".format(obj.price)
        return format_html(formatted_price)

# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     list_display = (
#         'status',
#     )

@admin.register(Type)
class TypeAdmin(ModelAdmin):
    list_display = (
        'types',
    )

@admin.register(Listing)
class ListingAdmin(ModelAdmin):
    list_display = (
        "types",
    )

@admin.register(Amenity)
class AmenityAdmin(ModelAdmin):
    list_display = (
        "amenity",
    )

@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    list_display = ('property',)

    def property(self, obj):
        return  f'{obj.property_name.landlord} Property {obj.property_name.street}'
