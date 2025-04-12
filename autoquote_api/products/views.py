from rest_framework import exceptions
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from .serializers import InventorySerializer


class ProductListCreateView(ListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class InventoryRetrieveView(RetrieveAPIView):
    model = Product
    serializer_class = InventorySerializer
    queryset = Product.objects.all()
