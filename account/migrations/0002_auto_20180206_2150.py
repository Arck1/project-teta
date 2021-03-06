# Generated by Django 2.0.2 on 2018-02-06 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
