# Generated by Django 3.2.7 on 2021-12-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20211229_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
