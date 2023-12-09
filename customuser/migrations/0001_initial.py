# Generated by Django 5.0 on 2023-12-09 20:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distric', models.CharField(blank=True, max_length=125)),
                ('department', models.CharField(blank=True, max_length=80)),
                ('reference', models.CharField(blank=True, max_length=150)),
                ('direction', models.CharField(blank=True, max_length=300)),
                ('phone', models.CharField(max_length=20)),
                ('postal_code', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
