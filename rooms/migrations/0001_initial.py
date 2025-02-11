# Generated by Django 5.1.5 on 2025-01-24 12:34

import django.db.models.deletion
import shared.file_utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0002_alter_hotelimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(upload_to=shared.file_utils.file_upload_path, validators=[shared.file_utils.validate_five_mb_image_size])),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=shared.file_utils.file_upload_path, validators=[shared.file_utils.validate_five_mb_image_size])),
            ],
            options={
                'db_table': 'room_types',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_beds', models.PositiveBigIntegerField()),
                ('total_capacity', models.PositiveBigIntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
                ('images', models.ManyToManyField(related_name='hotels', to='rooms.roomimages')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.roomtypes')),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
    ]
