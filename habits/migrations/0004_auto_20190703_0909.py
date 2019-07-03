# Generated by Django 2.2.3 on 2019-07-03 13:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0003_auto_20190703_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='buddy',
        ),
        migrations.AddField(
            model_name='habit',
            name='buddies',
            field=models.ManyToManyField(related_name='habits', to=settings.AUTH_USER_MODEL),
        ),
    ]
