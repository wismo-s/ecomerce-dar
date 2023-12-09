# Generated by Django 5.0 on 2023-12-09 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('port_img', models.ImageField(upload_to='products/files/port')),
                ('firts_img', models.ImageField(upload_to='products/files/baner')),
                ('second_img', models.ImageField(blank=True, null=True, upload_to='products/files/baner')),
                ('third_img', models.ImageField(blank=True, null=True, upload_to='products/files/baner')),
                ('four_img', models.ImageField(blank=True, null=True, upload_to='products/files/baner')),
                ('sold', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('choises', models.ManyToManyField(to='products.choises')),
            ],
        ),
    ]