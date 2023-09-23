from django.shortcuts import render

# Create your views here.


def LessonsView(request):
    context = {
        'title': 'Уроки',
    }

    return render(request, 'lessons/lessons.html', context)