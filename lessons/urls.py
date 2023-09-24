
from django.urls import path
from .views import LessonView
from . import views


app_name = 'lessons'

urlpatterns = [
    path('', LessonView, name='lessons'),
    path('lessons/', views.LessonList.as_view(), name='lessons_list'),
]