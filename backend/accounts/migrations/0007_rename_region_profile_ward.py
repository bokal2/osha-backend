# Generated by Django 4.0.3 on 2022-05-16 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_profile_attachment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='region',
            new_name='ward',
        ),
    ]
