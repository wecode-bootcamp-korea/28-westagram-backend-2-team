from django.db import models

# Create your models here.

class User(models.Model):
    email         = models.CharField(max_length=100, unique=True)
    mobile        = models.CharField(max_length=20, unique=True)
    user_name     = models.CharField(max_length=100)
    user_id       = models.CharField(max_length=100, unique=True)
    password      = models.CharField(max_length=256)
    birth_date    = models.DateField(null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)    
    
    class Meta:
        db_table = 'users'
    