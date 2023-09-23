from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='products')
    accesses = models.ManyToManyField('users.User', blank=True, related_name='accesses_to')