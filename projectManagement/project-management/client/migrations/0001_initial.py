# Generated by Django 5.0.7 on 2024-07-11 13:56

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
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
                ('client_id', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.PositiveBigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('address', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
