from django.db        import models
from django.db.models import Model

# Create your models here.
class User(models.Model):
    name                     = models.CharField(max_length=45)
    email                    = models.EmailField(max_length=128, null=False, unique=True)
    password                 = models.CharField(max_length=200, null=False)
    phon_number              = models.CharField(max_length=11, null=False)
    business_number          = models.CharField(max_length=50, blank=True)
    is_allowing_email_recive = models.BooleanField(default=True)
    is_enterprize            = models.BooleanField(default=True)
    personal_site            = models.URLField(max_length=200, blank=True)
    created_at               = models.DateField(auto_now_add=True)
    updated_at               = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'