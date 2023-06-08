from django.shortcuts import render
from rest_framework import viewsets
from charts.models import Product
from charts.serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    print(queryset)
    serializer_class=ProductSerializer

