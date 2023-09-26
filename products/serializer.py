from rest_framework import serializers
from .models import Product


class ProductStatisticsSerializer(serializers.ModelSerializer):
    total_watched_lessons = serializers.IntegerField()
    total_viewing_time = serializers.IntegerField()
    total_students = serializers.IntegerField()
    product_purchase_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Product
        fields = ['id', 'name', 'total_watched_lessons', 'total_viewing_time', 'total_students', 'product_purchase_percentage']