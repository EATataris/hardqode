from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializer import ProductSerializer
# Create your views here.


def ProductView(request):
    context = {
        'title': 'Продукты',
    }

    return render(request, 'products/products.html', context)


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]