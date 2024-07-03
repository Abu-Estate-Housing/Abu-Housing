

from rest_framework import serializers


class ListPropertySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    property_type = serializers.SerializerMethodField()
    status = serializers.CharField()
    price = serializers.IntegerField()
    bedroom = serializers.CharField()
    bathroom = serializers.CharField()
    amenities = serializers.SerializerMethodField()
    street = serializers.CharField()
    description = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()
    city = serializers.CharField()
    state = serializers.CharField()


    def get_property_type(self, obj):
        return obj.property_type.types

    def get_description(self, obj):
        return obj.description[:30]

    def get_amenities(self, obj):
        amenities = obj.amenity.all()
        return [amenity.amenity for amenity in amenities]

    def get_photos(self, obj):
        photos = obj.photo_set.all()
        return [photo.image.url for photo in photos]
