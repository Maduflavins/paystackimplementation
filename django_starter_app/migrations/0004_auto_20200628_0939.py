# Generated by Django 3.0.5 on 2020-06-28 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_starter_app', '0003_auto_20200628_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='email',
        ),
    ]
