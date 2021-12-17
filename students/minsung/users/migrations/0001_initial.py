# Generated by Django 4.0 on 2021-12-16 10:27

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
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('password', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]