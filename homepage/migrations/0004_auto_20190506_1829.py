# Generated by Django 2.2 on 2019-05-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_data_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
