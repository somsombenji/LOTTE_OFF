# Generated by Django 3.1.2 on 2020-10-12 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20201012_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='drive',
        ),
    ]
