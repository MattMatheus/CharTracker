# Generated by Django 5.0.1 on 2024-01-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuthDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scope', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
                ('refresh_token', models.CharField(max_length=200)),
            ],
        ),
    ]
