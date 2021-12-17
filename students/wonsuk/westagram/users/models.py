from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    other_information = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'users'