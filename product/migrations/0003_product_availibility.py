# Generated by Django 5.1.1 on 2024-09-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availibility',
            field=models.BooleanField(default=True),
        ),
    ]
