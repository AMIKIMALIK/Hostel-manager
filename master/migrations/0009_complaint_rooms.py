# Generated by Django 3.1.2 on 2021-01-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_auto_20210108_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=10)),
                ('floor', models.CharField(max_length=10)),
                ('block', models.CharField(max_length=10)),
                ('room_type', models.CharField(max_length=10)),
                ('room_capacity', models.CharField(max_length=10)),
                ('room_availablity', models.CharField(max_length=10)),
                ('studentid_1st', models.CharField(max_length=10)),
                ('studentid_2nd', models.CharField(max_length=10)),
                ('studentid_3rd', models.CharField(max_length=10)),
            ],
        ),
    ]
