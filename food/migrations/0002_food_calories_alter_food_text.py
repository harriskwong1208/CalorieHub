# Generated by Django 4.1.7 on 2023-07-21 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
