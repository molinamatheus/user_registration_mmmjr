from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=256, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    birthday = models.DateTimeField(auto_now_add=False)
    