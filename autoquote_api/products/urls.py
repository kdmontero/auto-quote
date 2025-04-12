from django.urls import path

from .views import ProductListCreateView


app_name = 'products'

urlpatterns = [
    path('', ProductListCreateView.as_view())
]