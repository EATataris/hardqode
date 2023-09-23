from django.shortcuts import render

# Create your views here.


def UserLessonView(request):
    context = {
        'title': 'Уроки пользователя',
    }

    return render(request, 'user_lessons/user_lessons.html', context)