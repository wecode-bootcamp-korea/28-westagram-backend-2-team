# Generated by Django 4.0 on 2021-12-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phon_number', models.CharField(max_length=11)),
                ('business_number', models.CharField(blank=True, max_length=50)),
                ('allowing_email_recive', models.BooleanField(default=True)),
                ('enterprize', models.BooleanField(default=True)),
                ('personal_site', models.URLField(blank=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
