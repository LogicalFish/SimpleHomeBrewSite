# Generated by Django 2.1.5 on 2019-01-28 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brew', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=26)),
                ('summary', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('jobs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brew.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
