from django.urls import path

from .views import ProductListCreateView
from .views import ProductRetrieveUpdateDestroyView


app_name = 'products'

urlpatterns = [
    path('', ProductListCreateView.as_view()),
    path('<pk>/', ProductRetrieveUpdateDestroyView.as_view()),
]