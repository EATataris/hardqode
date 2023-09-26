from django.urls import path
from .views import ProductView
from . import views

app_name = 'products'

urlpatterns = [
    path('', ProductView, name='products'),
    path('products_statistics/', views.ProductStatisticsList.as_view(), name='products_statistics_list'),
]