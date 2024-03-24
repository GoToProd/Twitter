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
        form = CreateNewTweet(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            text_tweet = form.cleaned_data['text_tweet']
            Tweet.objects.create(author=author, text_tweet=text_tweet)
            return redirect('index')
    else:
        form = CreateNewTweet()

    context = {
        'title': 'Twitter - Новый твит',
        'form': form,
    }

    return render(request, 'twit/add_tweet.html', context)
