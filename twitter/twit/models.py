from django.db import models


class Tweet(models.Model):
    author = models.CharField(max_length=32, null=False, blank=False, default='Anonymouse')
    text = models.TextField(max_length=255, blank=False, null=False)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'