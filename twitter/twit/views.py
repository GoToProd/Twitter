from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import redirect, render


from twit.forms import CreateNewTweet
from twit.models import Tweet

def index(request):
    
    tweets = Tweet.objects.all()
    
    context = {
        'title': 'Twitter - Главная',
        'tweets': tweets,
    }
    
    return render(request, 'index.html', context)


def add_tweet(request):
    if request.method == 'POST':
        form = CreateNewTweet(data=request.POST)
        if form.is_valid():
            try:
                Tweet.objects.create(
                    author = request.author,
                    text_tweet = request.text_tweet,
                )

                Tweet.save()                        
                return redirect('index')
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('twit:add_tweet')
    # else:
        # initial = {
        #     'author': request.author,
        #     'text_tweet': request.text_tweet,
        # }
        
        # form = CreateNewTweet(initial=initial)

    context = {
        'title': 'Twitter - Новый твит'
    }

    return render(request, 'twit/add_tweet.html', context)