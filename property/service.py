
from .models import Property


class PropertyService:

    @staticmethod
    def get_properties():
        return Property.objects.filter(status=Property.AVAILABLE)
