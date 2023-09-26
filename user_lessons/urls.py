from django.urls import path
from .views import UserLessonView
from . import views

app_name = 'user_lessons'

urlpatterns = [
    # path('', UserLessonView, name='user_lessons'),
    path('user_lessons/', views.UserLessonsList.as_view(), name='user_lessons_list'),
    path('product_lessons/<int:product_id>/', views.ProductLessonsList.as_view(), name='product_lessons_list'),
]
