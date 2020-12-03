from django.db import models
from django.contrib.auth.models import User 
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Tweet(models.Model):
    body = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField()

    def __str__(self):
        return self.body
    
class Hashtag(models.Model):
    tagName = models.CharField(max_length=140)
    tweets = ArrayField(models.CharField())

    
