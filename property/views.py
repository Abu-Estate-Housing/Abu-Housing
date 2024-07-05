from rest_framework import generics, status

from property.serializer import ListPropertySerializer
from property.service import PropertyService
from utils import CustomResponse


class ListPropertyView(generics.GenericAPIView):
    serializer_class = ListPropertySerializer 

    def get(self, request):
        properties = PropertyService.get_properties()
        properites = self.serializer_class(properties, many=True).data
        return CustomResponse(data=properites, status=status.HTTP_200_OK)

