from django.db import models
from django.utils import timezone
import datetime



class User(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    birthday = models.DateTimeField('date of birth')
    
    def __str__(self):
        return self.name
    

class MetaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='myuser')
    friends = models.ManyToManyField(User, blank=True)

