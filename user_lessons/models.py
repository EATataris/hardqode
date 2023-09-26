from django.db import models
from lessons.models import Lesson
from users.models import User
from products.models import Product
# Create your models here.


class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    viewing_time = models.IntegerField()
    status = models.CharField(max_length=20, choices=(('watched', 'Просмотрено'), ('not_watched', 'Не просмотрено')))
    last_viewed_at = models.DateTimeField(null=True, blank=True)