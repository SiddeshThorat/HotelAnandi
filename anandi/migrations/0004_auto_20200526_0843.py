# Generated by Django 3.0.5 on 2020-05-26 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anandi', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cus_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
