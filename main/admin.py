from django.contrib import admin
from main.models import Tweet
from main.models import Hashtag, UserLikes
# Register your models here.

admin.site.register(Tweet)
admin.site.register(Hashtag)
admin.site.register(UserLikes)