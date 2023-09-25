from rest_framework import serializers
from .models import UserLesson


class UserLessonSerializer(serializers.ModelSerializer):
    # last_viewed_at = serializers.DateTimeField(source='get_last_viewed_at', read_only=True)
    class Meta:
        model = UserLesson
        fields = ['lesson', 'status', 'viewing_time', 'last_viewed_at']