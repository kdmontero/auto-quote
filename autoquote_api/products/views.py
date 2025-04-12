from rest_framework import exceptions
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(ListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
