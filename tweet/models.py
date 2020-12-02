from django.db import models

# Create your models here.
class User(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.DecimalField(max_digits=6, decimal_places=0)