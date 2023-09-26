from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Lesson
from .serializers import LessonSerializer

# Create your views here.


def LessonView(request):
    context = {
        'title': 'Уроки',
    }

    return render(request, 'lessons/lessons.html', context)


class LessonList(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

