# Generated by Django 3.2.7 on 2021-12-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20211226_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
