from django.db import models

class User(models.Model):
    name          = models.CharField(max_length=50)
    email         = models.CharField(max_length=100, unique=True)
    password      = models.CharField(max_length=256)
    phone_number  = models.CharField(max_length=30, unique=True)
    date_of_birth = models.DateField(null=True)

    class Meta:
        db_table = 'users'

