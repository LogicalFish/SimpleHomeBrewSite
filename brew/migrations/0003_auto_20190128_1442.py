# Generated by Django 2.1.5 on 2019-01-28 14:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brew', '0002_brews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brews',
            new_name='Homebrew',
        ),
    ]
