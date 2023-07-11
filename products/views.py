from django.shortcuts import render


def index(request):
    context = {
        'title': 'Магазин одежды - тест',
        'username': 'Вася'
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    return render(request, 'products/products.html')
