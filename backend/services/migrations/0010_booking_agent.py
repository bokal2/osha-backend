# Generated by Django 4.0.3 on 2022-05-30 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
        ('services', '0009_ward'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agents.agent'),
        ),
    ]
