# Generated by Django 4.1.7 on 2023-07-27 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_food_calories_alter_food_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='created',
            field=models.DateTimeField(auto_created=True, blank=True),
        ),
    ]
