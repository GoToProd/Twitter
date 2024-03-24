from django.shortcuts import render


def index(request):
    
    context = {
        'title': 'Twitter - Главная',
    }
    
    return render(request, 'base.html', context)