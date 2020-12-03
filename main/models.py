from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class UserLikes(models.Model): #potentiall need this
    # current = models.IntegerField()
    user = models.CharField(max_length=200, default='')
    # tweet = models.OneToOneField(Tweet, on_delete=models.DO_NOTHING)
    # tweet = models.IntegerField()


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(UserLikes)
    # likes = models.IntegerField()
    # userlikes = models.ManyToManyField("self")

    def __str__(self):
        return self.body  


class Hashtag(models.Model):
    body = models.CharField(max_length=140)
    hashToTweet = models.ManyToManyField(Tweet)
    
    def __str__(self):
        return self.body

