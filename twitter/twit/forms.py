from django import forms


class CreateNewTweet(forms.Form):
    
    author = forms.CharField()
    text_tweet = forms.TextInput()
    