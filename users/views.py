from django.shortcuts import render

# Create your views here.


def UserView(request):
    context = {
        'title': 'Профиль',
    }

    return render(request, 'users/user.html', context)