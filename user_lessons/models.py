from django.db import models

# Create your models here.


class UserLesson(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=(('watched', 'Просмотрено'), ('not_watched', 'Не просмотрено')))