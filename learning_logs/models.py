from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.

""" A topic the user is learning about """
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        """ Return a string representation of the model """
        return self.text





class Entry(models.Model):

    """ Somthing specific learned about a topic"""
    topic = models.ForeignKey ( Topic, on_delete= models.CASCADE)
    
    text = models.TextField( )
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """ Return a string representaion of the model """
        
        return "{self.text[:50]}"
        



        