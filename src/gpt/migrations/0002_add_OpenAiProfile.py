# Generated by Django 3.2.18 on 2023-06-16 05:44

import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt', '0001_add_Reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenAiProfile',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=100)),
                ('usage_count', models.PositiveIntegerField(default=0)),
                ('comment', models.TextField(default='')),
                ('status', models.CharField(choices=[('active', 'Active'), ('archived', 'Archived')], default='active', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]