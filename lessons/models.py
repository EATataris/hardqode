from django.db import models

# Create your models here.


class Lesson(models.Model):
    title = models.CharField(max_length=64, unique=True)
    video_url = models.URLField()
    duration = models.DurationField()