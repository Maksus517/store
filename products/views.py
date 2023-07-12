from django.shortcuts import render


def index(request):
    context = {
        'title': 'Магазин одежды - тест'
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'Каталог - тест'
    }
    return render(request, 'products/products.html', context=context)
