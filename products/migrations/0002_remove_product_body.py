# Generated by Django 2.0.2 on 2018-04-20 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='body',
        ),
    ]
