from django.urls import path
from .views import ProductView


app_name = 'products'

urlpatterns = [
    path('', ProductView, name='products'),
]