# Generated by Django 3.0.5 on 2021-01-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0012_auto_20210112_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='datetime',
            field=models.CharField(default='2021-01-14', max_length=20),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date_time',
            field=models.DateField(default='2021-01-14'),
        ),
    ]
