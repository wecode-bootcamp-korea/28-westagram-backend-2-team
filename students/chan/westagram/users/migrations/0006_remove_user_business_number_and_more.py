# Generated by Django 4.0 on 2021-12-21 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='business_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_allowing_email_recive',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_enterprize',
        ),
        migrations.RemoveField(
            model_name='user',
            name='personal_site',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
