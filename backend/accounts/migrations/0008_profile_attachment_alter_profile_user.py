# Generated by Django 4.0.3 on 2022-05-23 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_rename_region_profile_ward'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='attachment',
            field=models.ImageField(default='default.jpg', upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
