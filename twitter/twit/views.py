from django.shortcuts import render


from twit.models import Tweet

def index(request):
    
    tweets = Tweet.objects.all()
    
    context = {
        'title': 'Twitter - Главная',
        'tweets': tweets,
    }
    
    return render(request, 'index.html', context)


def add_tweet(request):
    # tweet = request.POST.get('text')
    context = {
        'title': 'Twitter - Новый твит'
    }

    return render(request, 'twit/add_tweet.html', context)