from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserLesson
from .serializers import UserLessonSerializer
# Create your views here.


def UserLessonView(request):
    context = {
        'title': 'Уроки пользователя',
    }

    return render(request, 'user_lessons/user_lessons.html', context)


class UserLessonsList(generics.ListAPIView):
    queryset = UserLesson.objects.all()
    serializer_class = UserLessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserLesson.objects.filter(user=user)