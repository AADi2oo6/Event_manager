from django.db import models

# Create your models here.
class login(models.Model):
    
    uname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=10)