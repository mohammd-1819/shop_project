# Generated by Django 5.1.1 on 2024-09-21 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_productreview_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='created_at',
        ),
    ]
