from django.db        import models
from django.db.models import Model

class User(models.Model):
    name         = models.CharField(max_length=45)
    email        = models.EmailField(max_length=128, unique=True)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    address      = models.CharField(max_length=500, null=True)
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'