from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Tweet(models.Model):
    body = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now=True)
    userlikes = models.ManyToManyField("self")
    likes = models.IntegerField()
    userlikes = models.ManyToManyField("self")

    def __str__(self):
        return self.body
# class UserLikes(models.Model): potentiall need this

class Hashtag(models.Model):
    body = models.CharField(max_length=140)
    hashToTweet = models.ManyToManyField(Tweet)

