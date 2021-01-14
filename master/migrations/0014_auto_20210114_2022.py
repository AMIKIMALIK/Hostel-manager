# Generated by Django 3.0.5 on 2021-01-14 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0013_auto_20210114_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='student_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]
