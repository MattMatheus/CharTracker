# Generated by Django 5.0.1 on 2024-01-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyCharProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_name', models.CharField(max_length=16)),
                ('superbloom', models.BooleanField()),
                ('rep_weekly', models.BooleanField()),
                ('dream_seeds', models.BooleanField()),
            ],
        ),
    ]
