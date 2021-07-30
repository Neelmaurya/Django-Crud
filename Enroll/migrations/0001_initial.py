# Generated by Django 3.1.2 on 2021-07-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('dob', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=35)),
                ('mobile', models.CharField(max_length=10)),
                ('pwd', models.CharField(max_length=15)),
                ('cpwd', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('dob', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=35)),
                ('mobile', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
