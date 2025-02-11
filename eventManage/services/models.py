from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100, default='NA')
    volunteer = models.CharField(max_length=100, default='NA')
    date = models.DateField()
    description = models.TextField()

class Ticket(models.Model):

    name = models.CharField(max_length=255)
    event = models.CharField(max_length=100, default='NA')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class volunteer(models.Model):
    name = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
