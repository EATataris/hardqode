from django.shortcuts import render

# Create your views here.


def ProductView(request):
    context = {
        'title': 'Продукты',
    }

    return render(request, 'products/products.html', context)

