# Generated by Django 3.0.5 on 2020-05-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anandi', '0008_auto_20200530_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='bill',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
