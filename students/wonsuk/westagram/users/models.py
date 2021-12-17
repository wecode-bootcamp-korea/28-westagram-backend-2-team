from django.db import models

class User(models.Model):
    username          = models.CharField(max_length=50)
    email             = models.CharField(max_length=100, unique=True)
    password          = models.CharField(max_length=256)
    phone_number      = models.CharField(max_length=100)
    other_information = models.CharField(max_length=300, null=True)
    
    class Meta:
        db_table = 'users'