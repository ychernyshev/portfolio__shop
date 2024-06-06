from rest_framework import serializers

from ..models import ProductItemModel


class ProductItemSerializers(serializers.ModelSerializer):
    class Metea:
        model = ProductItemModel
        fields = '__all__'
