# Generated by Django 4.0.3 on 2022-05-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_ward'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='express',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
