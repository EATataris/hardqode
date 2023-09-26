from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product
from users.models import User
from .serializer import ProductStatisticsSerializer
from django.db.models import Sum, F, IntegerField, DurationField, DecimalField, ExpressionWrapper, Case, When
from django.db.models.functions import Coalesce, Cast
# Create your views here.


def ProductView(request):
    context = {
        'title': 'Продукты',
    }

    return render(request, 'products/products.html', context)


class ProductStatisticsList(generics.ListAPIView):
    serializer_class = ProductStatisticsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        products = Product.objects.annotate(
            total_watched_lessons=ExpressionWrapper(Sum(Coalesce(F('lessons__userlesson__status'), 0)),
                                                    output_field=IntegerField()),
            total_viewing_time=Sum('lessons__userlesson__viewing_time'), ).annotate(
            total_students=Sum(
                Case(When(owner__products=F('pk'), then=1), default=0, output_field=IntegerField()))).annotate(
            product_purchase_percentage=ExpressionWrapper((F('total_students') / User.objects.count()) * 100,
                                                          output_field=IntegerField()))
        return products
