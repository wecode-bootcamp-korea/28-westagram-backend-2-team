from django.db import models

# Create your models here.

class User(models.Model):
    email         = models.CharField(max_length=100, unique=True)
    mobile        = models.CharField(max_length=20, unique=True)
    user_name     = models.CharField(max_length=100)
    user_id       = models.CharField(max_length=100, unique=True)
    password      = models.CharField(max_length=256)
    birth_date    = models.DateField(null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    