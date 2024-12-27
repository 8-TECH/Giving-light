from django.db import models

# Create your models here.

class Program(models.Model):
    program = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.program 
    
    
class Event(models.Model):
    event = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.event
    