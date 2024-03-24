from django.contrib import admin


from twit.models import Tweet

# Register your models here.
# @admin.register(Tweet)
# class CartTabAdmin(admin.ModelAdmin):
#     model = Tweet
#     fields = ['author', 'created_timestamp', 'text',]
#     search_fields = ['author', 'created_timestamp']
#     readonly_fields = ['created_timestamp',]
#     extra = 1

admin.site.register(Tweet)