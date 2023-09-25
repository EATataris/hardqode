from django.db import models
from lessons.models import Lesson
from users.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    lessons = models.ManyToManyField(Lesson)
