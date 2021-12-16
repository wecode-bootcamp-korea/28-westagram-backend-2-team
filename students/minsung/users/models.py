from django.db import models

# Create your models here.

class User(models.Model):
    name         = models.CharField(max_length=100)
    email        = models.CharField(max_length=200)
    password     = models.IntegerField()
    phone_number = models.IntegerField()
    age          = models.IntegerField()

    class Meta:
        db_table = 'users'

