from rest_framework import serializers
from .models import UserLesson


class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLesson
        fields = '__all__'