# Generated by Django 5.0.1 on 2024-01-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weekly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklycharprogress',
            name='raidfinder_1',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weeklycharprogress',
            name='raidfinder_2',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weeklycharprogress',
            name='raidfinder_3',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weeklycharprogress',
            name='raidfinder_4',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
