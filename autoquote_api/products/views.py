from rest_framework.generics import ListCreateAPIView

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(ListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
