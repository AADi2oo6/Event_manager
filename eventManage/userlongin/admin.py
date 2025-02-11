from django.contrib import admin
from .models import login
from django.contrib.admin import ModelAdmin

class logindmin(admin.ModelAdmin):
    list_display = ['id','uname','email','password']
admin.site.register(login,logindmin)
