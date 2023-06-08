from rest_framework import serializers
from charts.models import Product

#create serializer here
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Product
        fields="__all__"