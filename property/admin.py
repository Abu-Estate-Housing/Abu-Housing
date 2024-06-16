from django.contrib import admin

from property.models import Amenity, Listing, Photo, Property, Status, Type

# Register your models here.
#
@admin.register(Property)
class ProprtyAdmin(admin.ModelAdmin):
    list_filter = ("status", "property_type", "listing")
    search_fields = ('occupant__email',)
    list_display = (
        "occupant", "bedroom", "bathroom", "price", "city", "street", "status"
    )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'status',
    )

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'types',
    )

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "types",
    )

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "amenity",
    )

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('property',)

    def property(self, obj):
        return  f'{obj.property_name.occupant} Property'
