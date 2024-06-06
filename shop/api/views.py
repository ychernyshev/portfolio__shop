from rest_framework.response import Response
from rest_framework import generics

from ..models import ProductItemModel
from .serializers import ProductItemSerializers


class ProductItemsView(generics.RetrieveAPIView):
    queryset = ProductItemModel.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductItemSerializers(queryset, many=True)
        return Response(serializer.data)


