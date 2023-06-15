# Generated by Django 3.2.18 on 2023-06-15 13:04

import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt', '0002_change_ordering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='id',
        ),
        migrations.AddField(
            model_name='reply',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
