# Generated by Django 3.2.18 on 2023-06-15 10:48

from django.conf import settings
from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('archived', 'Archived')], default='active', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('previous_reply', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_reply', to='gpt.reply')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
