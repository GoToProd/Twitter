from django.shortcuts import render


from twit.models import Tweet

def index(request):
    
    tweets = Tweet.objects.all()
    
    context = {
        'title': 'Twitter - Главная',
        'tweets': tweets,
    }
    
    return render(request, 'base.html', context)