from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Lesson
from .serializers import LessonSerializer
from products.models import Product
from users.models import User
from user_lessons.models import UserLesson
from django.core.exceptions import ObjectDoesNotExist
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

# def lessons_list(request, user_id=None):
#     if User.objects.filter(id=user_id).exists():
#         user = User.objects.get(id=user_id)
#     else:
#         return JsonResponse({"error": "User does not exist"}, status=404)
#
#     products = Product.objects.filter(accesses__in=user.accesses.all())
#
#     lessons = []
#     for product in products:
#         lessons.extend(product.lessons.all())
#
#     for lesson in lessons:
#         user_lesson = UserLesson.objects.filter(lesson=lesson, user=User.objects.get(id=user_id).first())
#
#         if user_lesson is not None:
#             lesson.status = user_lesson.status
#             lesson.start_time = user_lesson.start_time
#             lesson.end_time = user_lesson.end_time
#
#     return JsonResponse({"lessons": lessons})